def reversed_sentence(a_string:str)->str:
    lst_a_string = a_string.split(" ")
    res = []
    for i in range(len(lst_a_string)-1, -1, -1):
        res.append(lst_a_string[i])
    return " ".join(res)
print(reversed_sentence("You have entered a wrong domain"))

# time left: 24:50