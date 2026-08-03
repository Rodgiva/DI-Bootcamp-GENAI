txt = "I’ll build the coziest lantern\nTo help you cross the ocean\nI want to keep you dry\nI want to keep the spark\nAnd if the storm is hitting\nI’ll try to keep you steady\nAnd if I feel I‘m shaking\nI would return to practice\nAnd if my arm is hurting\nAnd I if I need to rest\nWe’d have to switch positions\nAnd you would do it well\nWe’d light the darkest forest\nBrighten our darkest sins\nWe’d light the deepest cave and\nEnlight the deepest meanings\nYou know I gave my breath so I could feed it\nI blew too hard I thought I killed it\nI saw an ember hidden in the ashes\nI’ll blow again if it can be ignited\nI’d build the strongest walls\n(So you could feel protected)\nMade of the purest glass\n(Cause you simply deserve it)\nI‘ll build the coziest home\n(And we would learn to live in)\nMade of the purest love\n(Cause you simply deserve it)\nAnd you could hear the rain banging the ceiling\nAnd not a single drop could stain our feelings\nAnd you could hear the rain banging the ceiling\nAnd not a single drop could stain our feelings\nYou gave me your trust cause you knew I could keep it\nThe fire’s so pure we could learn how to drink it\nYou gave me your heart cause you knew I could light it\nCause you know, cause you know\nCause you know, cause you know\nCause you know, cause you know\nOh, cause you know, cause you know"
def encrypt(txt: str, shift: int):
    res = ""
    for c in txt:
        res += chr(ord(c) + shift)
    return res

def decrypt(txt: str, shift: int):
    res = ""
    for c in txt:
        res += chr(ord(c) - shift)
    return res

def ceasar_cypher():
    msg = input("Give me the message: ")
    shift = int(input("And the shift key: "))
    while True:
        check = input("You want to encrypt(1) or decrypt(2)? ")
        if check == "1" or check == "encrypt":
            return encrypt(msg, shift)
        elif check == "2" or check == "decrypt":
            return decrypt(msg, shift)
        else:
            print("Again:")

print(ceasar_cypher())