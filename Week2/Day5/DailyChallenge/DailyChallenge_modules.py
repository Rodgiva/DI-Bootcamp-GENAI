import requests
import time

sites = ["https://www.google.com", "https://www.ynet.net", "https://www.imdb.com"]

for site in sites:
    try:
        start = time.time()
        res = requests.get(site)
    finally:
        end = time.time()
        seconds = end - start
        print(f"{site}: {seconds}")