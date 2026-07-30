import math

# EXERCICE 1

# --- difference ---
def difference(a, b):
    return a - b
print(difference(2,2))
print(difference(0,2))
print("----------------")

# --- print_day ---
def print_day(day):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return days.get(day, None)
print(print_day(4))
print(print_day(41))
print("----------------")

# --- last_element ---
def last_element(lst):
    return lst[-1] if lst else None
print(last_element([1,2,3,4]))
print(last_element([]))
print("----------------")

# --- number_compare ---
def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Numbers are equal"
print(number_compare(1, 1))
print(number_compare(1, 2))
print(number_compare(2, 1))
print("----------------")

# --- single_letter_count ---
def single_letter_count(word, letter):
    return word.lower().count(letter.lower())
print(single_letter_count('amazing','A'))
print("----------------")

# --- multiple_letter_count ---
def multiple_letter_count(word):
    dict = {
        k: word.count(k) for k in word
    }
    return dict
print(multiple_letter_count("hello"))
print(multiple_letter_count("person"))
print("----------------")

# --- list_manipulation ---
def list_manipulation(lst, command, location, value=None):
    if command == "remove":
        if location == "end":
            return lst.pop(-1)
        if location == "beginning":
            return lst.pop(0)
    if command == "add":
        if location == "end":
            lst.append(value)
            return lst
        if location == "beginning":
            lst.insert(0, value)
            return lst
print(list_manipulation([1,2,3], "remove", "end"))
print(list_manipulation([1,2,3], "remove", "beginning"))
print(list_manipulation([1,2,3], "add", "beginning", 20))
print(list_manipulation([1,2,3], "add", "end", 30))
print("----------------")

# --- is_palindrome ---
def is_palindrome(input_str):
    clean_str = input_str.replace(" ", "")
    for i in range(math.floor(len(clean_str)/2)):
        if clean_str[i] != clean_str[len(clean_str)-(i+1)]:
            return False
    return True
print(is_palindrome("testing"))
print(is_palindrome("tacocat"))
print(is_palindrome("hannah"))
print(is_palindrome("robert"))
print("----------------")

# --- frequency ---
def frequency(lst, search_term):
    return lst.count(search_term)
print(frequency([1,2,3,4,4,4], 4))
print(frequency([True, False, True, True], False))
print("----------------")

# --- flip_case ---
def flip_case(str, letter):
    res = ""
    for c in str:
        if c.lower() == letter.lower():
            res += c.swapcase()
        else:
            res += c
    return res
print(flip_case("Hardy har har", "h"))
print("----------------")

# --- multiply_even_numbers ---
def multiply_even_numbers(lst):
    res = 1
    for nb in lst:
        if nb % 2 == 0:
            res *= nb
    return res
print(multiply_even_numbers([2,3,4,5,6]))
print("----------------")

# --- mode ---
input_list = [2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]
def mode(lst):
    res_dict = {num: lst.count(num) for num in set(lst)}
    return max(res_dict, key=res_dict.get)
print(mode(input_list))
print("----------------")

# --- capitalize ---
def capitalize(str):
    return str.capitalize()
print(capitalize("tim"))
print(capitalize("matt"))
print("----------------")

# --- compact ---
def compact(lst):
    return [elem for elem in lst if elem]
print(compact([0,1,2,"",[], False, {}, None, "All done"]))
print("----------------")

# --- partition ---
def is_even(num):
    return num % 2 == 0

def partition(lst, callback):
    lst1 = []
    lst2 = []
    for elem in lst:
        if callback(elem) == True:
            lst1.append(elem)
        else:
            lst2.append(elem)
    return [lst1, lst2]
print(partition([1,2,3,4], is_even))
print("----------------")

# --- intersection ---
def intersection(lst1, lst2):
    return [
        x
        for x in lst1
        if x in lst2
    ]
print(intersection([1,2,3], [2,3,4]))
print("----------------")

# --- once ---
def add(a,b):
    return a + b

def once(fnc):
    def wrapp(*arg1, **arg2):
        if wrapp.check == False:
            wrapp.check = True
            return fnc(*arg1, **arg2)
        else:
            return None
    wrapp.check = False
    return wrapp

one_addition = once(add)
print(one_addition(2,2))
print(one_addition(2,2))
print(one_addition(12,200))

# --- Super bonus ---
def once(fnc):
    def wrapp(*arg1, **arg2):
        if wrapp.check == False:
            wrapp.check = True
            return fnc(*arg1, **arg2)
        else:
            return None
    wrapp.check = False
    return wrapp

@once
def add(a,b):
    return a + b

print(add(2,2))
print(add(2,2))
print(add(12,100))
print("----------------")


# EXERCICE 2

# --- reverse ---
def reverse(x):
    return x[::-1]
print(reverse("hello"))
print("----------------")

# --- benefactor ---
donations_lst = [14, 30, 5, 7, 9, 11, 15]
def avrg_calc(lst, avrg_goal):
    sum_lst = sum(lst)
    sum_goal = (len(lst)+1) * avrg_goal
    return sum_goal - sum_lst
print(avrg_calc(donations_lst, 30))
print("----------------")

# --- sum_seq ---
def sum_seq(begin, end, step):
    if begin > end:
        return 0
    res = 0
    for i in range(begin, end+1, step):
        res += i
    return res
print(sum_seq(2,2,2))
print(sum_seq(2,6,2))
print(sum_seq(1,5,1))
print(sum_seq(1,5,3))
print("----------------")

# --- diff ---
def diff(lst):
    if len(lst) <= 1:
        return 0
    lower = lst[0]
    higher = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > higher:
            higher = lst[i]
        elif lst[i] < lower:
            lower = lst[i]
    return higher - (lower)
print(diff([1,2,3,4]))
print(diff([1,2,3,-4]))
print("----------------")

# --- countSmileys ---
def countSmileys(arr):
    res = 0
    valid_eyes = [":", ";"]
    valid_nose  = ["-", "~"]
    valid_mouth = [")", "D"]
    for i in range(len(arr)):
        if arr[i][0] in valid_eyes:
            if arr[i][1] in valid_nose:
                if arr[i][2] in valid_mouth:
                    res += 1
            elif arr[i][1] in valid_mouth:
                res += 1
    return res
print(countSmileys([':)', ';(', ';}', ':-D']))
print(countSmileys([';D', ':-(', ':-)', ';~)']))
print(countSmileys([';]', ':[', ';*', ':$', ';-D']))
print("----------------")

# --- count_sentenses ---
def count_sentenses(txt):
    return txt.count(".") + txt.count("?") + txt.count("!")
txt = "Spinal cord stroke is a rare type of stroke with compromised blood flow to any region of spinal cord owing to occlusion or bleeding, leading to irreversible neuronal death.[1] It can be classified into two types, ischaemia and haemorrhage, in which the former accounts for 86% of all cases, a pattern similar to cerebral stroke.[2][3] The disease is either arisen spontaneously from aortic illnesses or postoperatively.[4] It deprives patients of motor function or sensory function, and sometimes both.[5] Infarction usually occurs in regions perfused by anterior spinal artery, which spans the anterior two-thirds of spinal cord.[6] Preventions of the disease include decreasing the risk factors and maintaining enough spinal cord perfusion pressure during and after the operation. The process of diagnosing the ischemic and hemorrhagic spinal cord stroke includes applying different MRI protocols and CT scan.[7][8] Treatments for spinal cord stroke are mainly determined by the symptoms and the causes of the disease. For example, antiplatelet and corticosteroids might be used to reduce the risk of blood clots in ischaemic spinal stroke patients, while rapid surgical decompression is applied to minimize neurological injuries in haemorrhagic spinal stroke patients instead.[9] Patients may spend years for rehabilitation after the spinal cord stroke.[3]"
print(count_sentenses(txt))
print("----------------")

# --- tortoise racing ---
def race(v1, v2, g):
    if v1 >= v2:
        return None
    v_diff = v2 - v1
    time = g / v_diff
    hour = math.floor(time)
    minute = math.floor((time * 60) % 60)
    second = math.floor((time * 3600) % 60)
    return [hour, minute, second]
print(race(720, 850, 70))
print(race(80, 91, 37))
print("----------------")

# --- string_rotation ---
def string_rotation(str1, str2):
    lst1 = list(str1)
    rot_lst = list(lst1)
    for i in range(len(lst1)):
        if "".join(rot_lst) == str2:
            return i
        for j in range(len(lst1)):
            if j < len(lst1)-1:
                rot_lst[j+1] = lst1[j]
            else:
                rot_lst[0] = lst1[j]
        lst1 = list(rot_lst)
    return -1
print(string_rotation("coffee", "eecoff"))
print(string_rotation("eecoff", "coffee"))
print(string_rotation("moose", "Moose"))
print(string_rotation("isn't", "'tisn"))
print(string_rotation("Esham", "Esham"))
print(string_rotation("dog", "god"))
print("----------------")
