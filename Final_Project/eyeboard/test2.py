import cv2
import numpy as np
from collections import deque

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("webcam inaccessible")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('haarcascade_eye.xml')

if face_cascade.empty() or eye_cascade.empty():
    raise RuntimeError("cascade non chargée")

noyau = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
hists = [deque(maxlen=5), deque(maxlen=5)]   # un historique par oeil

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10, minSize=(25, 25))
        eyes = sorted(eyes, key=lambda e: e[0])[:2]

        for i, (ex, ey, ew, eh) in enumerate(eyes):
            # rogner les bords (cils, paupieres)
            mx, my = int(ew * 0.20), int(eh * 0.20)
            eye_gray = roi_gray[ey+my : ey+eh-my, ex+mx : ex+ew-mx]
            if eye_gray.size == 0:
                continue

            blurred = cv2.GaussianBlur(eye_gray, (5, 5), 0)

            seuil = np.percentile(blurred, 15)
            _, thresh = cv2.threshold(blurred, seuil, 255, cv2.THRESH_BINARY_INV)

            thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, noyau)
            thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, noyau)

            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_SIMPLE)

            # garder les contours assez grands et assez circulaires
            candidats = []
            for c in contours:
                aire  = cv2.contourArea(c)
                perim = cv2.arcLength(c, True)
                if aire < 30 or perim == 0:
                    continue
                circularite = 4 * np.pi * aire / (perim ** 2)
                if circularite > 0.6:
                    candidats.append((aire, c))

            if not candidats:
                continue

            candidats.sort(reverse=True, key=lambda t: t[0])
            (cx, cy), radius = cv2.minEnclosingCircle(candidats[0][1])

            # passage en coordonnees absolues (image complete)
            gx = x + ex + mx + int(cx)
            gy = y + ey + my + int(cy)
            radius = int(radius)

            # lissage temporel, par oeil
            hists[i].append((gx, gy))
            hp = hists[i]
            gx = int(sum(p[0] for p in hp) / len(hp))
            gy = int(sum(p[1] for p in hp) / len(hp))

            cv2.circle(frame, (gx, gy), radius, (255, 0, 0), 2)
            cv2.line(frame, (gx - 10, gy), (gx + 10, gy), (0, 255, 0), 1)
            cv2.line(frame, (gx, gy - 10), (gx, gy + 10), (0, 255, 0), 1)

    cv2.imshow('Pupil Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()