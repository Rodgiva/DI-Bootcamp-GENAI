MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''

# --- Step 1: Transforming the String into a 2D List  ---
matrix_list = MATRIX_STR.split("\n")
matrix_list = [line for line in matrix_list if line]
print(matrix_list)
print("--------------------------")

# --- Step 2: Processing Columns  ---
# --- Step 3: Filtering Alpha Characters  ---
# --- Step 4: Replacing Symbols with Spaces  ---
# --- Step 5: Constructing the Secret Message ---
msg = ""
for i in range(len(matrix_list[0])):
    for j in range(len(matrix_list)):
        if 65 <= ord(matrix_list[j][i]) <= 122:
            msg += matrix_list[j][i]
        else:
            msg += " "
print(msg)
print("--------------------------")

