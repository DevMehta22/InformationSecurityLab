plaintext = input("Enter the plaintext:")
key = 3

plaintext = plaintext.replace(" ","")

map_table = {
    0:'&',1:'o',2:'p',
    3:'q',4:'r',5:'s',
    6:'t',7:'u',8:'v',
    9:'w',10:'x',11:'y',
    12:'z',13:'a',14:'b',
    15:'c',16:'d',17:'e',
    18:'f',19:'g',20:'h',
    21:'i',22:'j',23:'k',
    24:'l',25:'m',26:'n'
}

reversed_map = {value: key for key, value in map_table.items()}

def encrypt(plaintext,key):
    matrix = [['\n'for i in range(len(plaintext))] for j in range(key)]
    row,col = 0,0
    dir = False

    for i in plaintext:
        if(row == 0) or (row == key-1):
            dir = not dir
        matrix[row][col] = i
        col+=1
        
        if dir:
            row+=1
        else:
            row-=1

    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if(matrix[i][j] != '\n'):
                result.append(matrix[i][j])
    
    temp = result[0]
    result[0] = result[len(result)-1]
    result[len(result)-1] = temp
    
    mid_cipher = "".join(result)
    cipher=""
    for i in mid_cipher:
        j = ord(i.upper()) - 65
        cipher += map_table[j]

    return cipher

def decrypt(ciphertext,key):
    mid_cipher=""
    
    for i in ciphertext:
        j = chr(reversed_map[i]+65).lower()
        mid_cipher+=j
    list_cipher = list(mid_cipher)
    temp = list_cipher[0]
    list_cipher[0] = list_cipher[len(list_cipher)-1]
    list_cipher[len(list_cipher)-1] = temp
    
    mid_cipher="".join(list_cipher)
        
    matrix = [['\n' for i in range(len(mid_cipher))] for j in range(key)]
    row,col = 0,0
    
    for i in range(len(mid_cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        matrix[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(mid_cipher)):
            if ((matrix[i][j] == '*') and
            (index < len(mid_cipher))):
                matrix[i][j] = mid_cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(mid_cipher)):

        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False

        if (matrix[row][col] != '*'):
            result.append(matrix[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

ciphertext = encrypt(plaintext,key)
decyptedtext = decrypt(ciphertext,key)

print("EncryptedText:",ciphertext)
print("DecryptedText:",decyptedtext)


