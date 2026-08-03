# --- Challenge 1: Letter Index Dictionary ---
#1
word = input("Give me a word: ")
#2
characters_dict = {}
for i in range(len(word)):
    if word[i] in characters_dict.keys():
        characters_dict[word[i]].append(i)
    else:
        characters_dict[word[i]] = [i]
print(characters_dict)
print("--------------------------")

# --- Challenge 2: Affordable Items ---
#1
wallet = 1500
items_purchase = {
    "pc": "1200$",
    "book": "20$",
    "phone": "300$",
    "car": "20000$",
    "pencil": "5$",
}
print(items_purchase)
#2
for k, v in items_purchase.items():
    items_purchase[k] = int(v.replace(", ", "").replace("$", ""))
print(items_purchase)
#3
basket = []
for k, v in items_purchase.items():
    if wallet > v:
        basket.append(k)
        wallet -= v
print(f"Wallet: {wallet}$\nBasket: {basket}")