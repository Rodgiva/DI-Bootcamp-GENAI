# --- Exercise 1 ---
a_list = list([None, None, None, None, None, None, None])
a_list.insert(3, "an item")
print(a_list)
print("--------------------------")

# --- Exercise 2 ---
a_string = "This is a string"
nb_space = a_string.count(" ")
print(f"nb space: {nb_space}")
print("--------------------------")

# --- Exercise 3 ---
a_string = "This IS a sTrInG"
nb_upper = len([i for i in list(a_string) if i.isupper()])
nb_lower = len([i for i in list(a_string) if i.islower()])
print(f"nb upper: {nb_upper}")
print(f"nb lower: {nb_lower}")
print("--------------------------")

# --- Exercise 4 ---
a_list = [1,5,4,2]
def my_sum(a_list:list)->int:
    res = 0
    for i in a_list:
        res += i
    return res
print(my_sum(a_list))
print("--------------------------")

# --- Exercise 5 ---
a_list = [0,1,200,3,50]
def find_max(a_list:list)->int:
    max = a_list[0]
    for i in a_list:
        if i > max:
            max = i
    return max
print(find_max(a_list))
print("--------------------------")

# --- Exercise 6 ---
def factorial(nb:int)->int:
    res = 1
    for i in range(1, nb+1):
        res *= i
    return res
print(factorial(4))
print("--------------------------")

# --- Exercise 7 ---
def list_count(a_list:list, a_string:str)->int:
    res = 0
    for i in a_list:
        if i == a_string:
            res += 1
    return res
print(list_count(['a','a','t','o'],'a'))
print("--------------------------")

# --- Exercise 8 ---
def norm(a_list:list)->int:
    res = 0
    for i in a_list:
        res += i**2
    return int(res**.5)
print(norm([1,2,2]))
print("--------------------------")

# --- Exercise 9 ---
def is_mono(a_list:list)->bool:
    sorted_list = list(a_list)
    sorted_list.sort()
    if sorted_list == a_list:
        return True
    sorted_list.sort(reverse=True)
    if sorted_list == a_list:
        return True
    return False

print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))
print("--------------------------")

# --- Exercise 10 ---
a_list = ["truc", "bidule", "machin", "anticonstitutionnellement", "ouai", "tartiflette"]
def longest_word(a_list:list)->str:
    word = a_list[0]
    for w in a_list:
        if len(w) > len(word):
            word = w
    return word
print(longest_word(a_list))
print("--------------------------")

# --- Exercise 11 ---
int_list = []
str_list = []
a_list = [3, "hello", 57, "there", "machin", 352, 128, "courgette", 18]
for i in a_list:
    if type(i) is int:
        int_list.append(i)
    elif type(i) is str:
        str_list.append(i)
print(int_list)
print(str_list)
print("--------------------------")

# --- Exercise 12 ---
def is_palindrome(a_string:str)->bool:
    list_a_string = list(a_string)
    list_a_string.pop(len(list_a_string) // 2)
    a_string = "".join(list_a_string)

    mid_index = len(a_string) // 2
    mid_start = a_string[:mid_index]
    mid_end = a_string[mid_index:][::-1]

    if mid_start == mid_end:
        return True
    return False
print(is_palindrome('radar'))
print(is_palindrome('John'))
print("--------------------------")

# --- Exercise 13 ---
sentence = 'Do or do not there is no try'
def sum_over_k(s:str, k:int)->int:
    return len(list(filter(lambda a: len(a)>=k, s.split(" "))))
print(sum_over_k(sentence, 3))
print("--------------------------")

# --- Exercise 14 ---
def dict_avg(a_dict:dict)->int:
    return int(sum(a_dict.values())/len(a_dict))
print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))
print("--------------------------")

# --- Exercise 15 ---
def common_div(a:int, b:int)->list:
    res = []
    lower = a if a-b < 0 else b
    for i in range(2, lower+1):
        if a%i == 0 and b%i == 0:
            res.append(i)
    return res
print(common_div(10,20))
print("--------------------------")

# --- Exercise 16 ---
def is_prime(nb: int)->bool:
    filtered_list = list(filter(lambda a: nb%a == 0, range(2, nb)))
    if len(filtered_list) > 0:
        return False
    return True
print(is_prime(11))
print("--------------------------")

# --- Exercise 17 ---
def weird_print(a_list:list)->list:
    res = []
    for i in range(len(a_list)):
        if (i)%2==0 and a_list[i]%2==0:
            res.append(a_list[i])
    return res
print(weird_print([1,2,2,3,4,5]))
print("--------------------------")

# --- Exercise 18 ---
def type_count(**kwargs)->dict:
    a_dict = {}
    for v in kwargs.values():
        a_type = type(v).__name__
        if a_type in a_dict:
            a_dict[a_type] += 1
        else:
            a_dict[a_type] = 1
    return a_dict
print(type_count(a=1,b='string',c=1.0,d=True,e=False))
print("--------------------------")

# --- Exercise 19 ---
def a_split(a_string:str, spliter:str = " ")->list:
    splited = []
    spliting_word = ""
    for c in a_string:
        if c == spliter:
            splited.append(spliting_word)
            spliting_word = ""
        else:
            spliting_word += c
    splited.append(spliting_word)
    return splited
print(a_split("Hello there!"))
print("--------------------------")

# --- Exercise 20 ---
pwd = "mypassword"
def password_converter(a_string:str)->str:
    return "".join(list(map(lambda a : "*", list(a_string))))

def password_converter2(a_string:str)->str:
    return "*" * len(a_string)
print(pwd)
print(password_converter(pwd))
print(password_converter2(pwd))
print("--------------------------")