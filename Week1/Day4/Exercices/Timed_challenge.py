def nb_occ(a_string:str, char:str)->int:
    return len(list(filter(lambda a: a.lower() == char.lower(), list(a_string))))
print(nb_occ("Programming is cool!", "o"))
print(nb_occ("This is a great example", "y"))

# Time left: 11:46