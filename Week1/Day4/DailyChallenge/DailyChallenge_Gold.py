MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

matrix_list = MATRIX_STR.split("\n")
matrix_list = [line for line in matrix_list if line]
print(matrix_list)
print("--------------------------")

msg = ""
flag = False
for i in range(len(matrix_list[0])):
    for j in range(len(matrix_list)):
        if matrix_list[j][i].isalpha():
            if flag:
                msg += " "
                flag = False
            msg += matrix_list[j][i]
        else:
                flag = True
print(msg)
print("--------------------------")

