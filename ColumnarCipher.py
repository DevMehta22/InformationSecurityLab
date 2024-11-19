import math

def encrypt(key,plaintext):
    key_len = len(key)
    num_rows = math.ceil(len(plaintext)/key_len)

    matrix=[[' ']*key_len for _ in range(num_rows)]

    index = 0

    for i in range(num_rows):
        for j in range(key_len):
            if(index<len(plaintext)):
                matrix[i][j] = plaintext[index]
                index+=1
            else:
                matrix[i][j] = 'X'

    index = 0
            
    key_list = sorted(list(key))
    col_order = [key.index(k) for k in key_list]

    ciphertext = ""
    for col in col_order:
        for row in range(num_rows):
            ciphertext += matrix[row][col]
            
    return ciphertext

def decrpyt(key,ciphertext):
    key_len = len(key)
    num_rows = math.ceil(len(ciphertext)/key_len)
    matrix=[[' ']*key_len for _ in range(num_rows)]
    index = 0
    key_list = sorted(list(key))
    col_order = [key.index(k) for k in key_list]
    
    for col in col_order:
        for row in range(num_rows):
            matrix[row][col] = ciphertext[index]
            index+=1
            
    plaintext=''
    for i in range(num_rows):
        for j in  range(key_len):
            plaintext+=matrix[i][j]
    
    for i in plaintext:
        if(i == 'X'):
            plaintext = plaintext.replace('X','')
            
    for i in space_list:
        plaintext = plaintext[:i] + " " + plaintext[i:]
    
    return plaintext
                
    
plaintext = input("Enter the text:")
space_list =[]
for i in range(len(plaintext)):
    if(plaintext[i]==" "):
        space_list.append(i)

plaintext = plaintext.replace(" ","")

key = "GERMAN"
print(plaintext)
ciphertext = encrypt(key,plaintext)
print("Ciphertext:",ciphertext)
print("Plaintext",decrpyt(key,ciphertext))


        

