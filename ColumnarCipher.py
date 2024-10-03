import math

def encrypt(key,plaintext):
    key_len = len(key)
    num_cols = math.ceil(len(plaintext)/key_len)

    matrix=[[' 'for _ in range(num_cols)]for _ in range(key_len)]

    index = 0

    for i in range(key_len):
        for j in range(num_cols):
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
        for row in range(num_cols):
            ciphertext += matrix[col][row]
            
    return ciphertext

def decrpyt(key,ciphertext):
    key_len = len(key)
    num_cols = math.ceil(len(ciphertext)/key_len)
    matrix=[[' 'for _ in range(num_cols)]for _ in range(key_len)]
    index = 0
    key_list = sorted(list(key))
    col_order = [key.index(k) for k in key_list]
    
    for col in col_order:
        for row in range(num_cols):
            matrix[col][row] = ciphertext[index]
            index+=1
            
    plaintext=''
    for i in range(key_len):
        for j in  range(num_cols):
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


        

