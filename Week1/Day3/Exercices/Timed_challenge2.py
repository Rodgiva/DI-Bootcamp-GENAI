def is_perfect_nb(nb:int)->bool:
    divisors = []
    for i in range(1, nb):
        if nb%i==0:
            divisors.append(i)
    if sum(divisors) == nb:
        return True
    return False
print(is_perfect_nb(6))
print(is_perfect_nb(10))

# Time left 25:17