# MATRIX_STR = '''
# 7ir
# Tsi
# h%x
# i ?
# sM# 
# $a 
# #t%'''

# matrix_list = MATRIX_STR.split("\n")
# matrix_list = [line for line in matrix_list if line]

# msg = ""
# flag = False
# for i in range(len(matrix_list[0])):
#     for j in range(len(matrix_list)):
#         if matrix_list[j][i].isalpha():
#             if flag:
#                 msg += " "
#                 flag = False
#             msg += matrix_list[j][i]
#         else:
#             flag = True
# msg = msg.strip()

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

def matrix_decoder(encoded_str: str)->str:
    matrix_list = encoded_str.split("\n")
    matrix_list = [line for line in matrix_list if line]
    res = ""
    for i in range(len(matrix_list[0])):
        for j in range(len(matrix_list)):
            if matrix_list[j][i].isalpha():
                res += matrix_list[j][i]
            else:
                res += " "
    return " ".join(res.split())

print(matrix_decoder(MATRIX_STR))
# print("--------------------------")

