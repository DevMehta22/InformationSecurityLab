plaintext = input("Enter the plaintext:")
key = 3

plaintext = plaintext.replace(" ","")

def encrypt(plaintext,key):
    matrix = [['\n'for i in range(len(plaintext))] for j in range(key)]

    row,col = 0,0
    flag = False

    for i in plaintext:
        if(row == 0) or (row == key-1):
            flag = not flag
        matrix[row][col] = i
        col+=1
        
        if flag:
            row+=1
        else:
            row-=1

    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if(matrix[i][j] != '\n'):
                result.append(matrix[i][j])

    return ("".join(result))

def decrypt(ciphertext,key):
    matrix = [['\n' for i in range(len(ciphertext))] for j in range(key)]
    row,col = 0,0
    flag = False
    for i in range(len(ciphertext)):
        if row == 0:
            flag = True
        if row == key - 1:
            flag = False

        matrix[row][col] = '*'
        col += 1

        if flag:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if ((matrix[i][j] == '*') and (index < len(ciphertext))):
                matrix[i][j] = ciphertext[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):

        if row == 0:
            flag = True
        if row == key-1:
            flag = False

        if (matrix[row][col] != '*'):
            result.append(matrix[row][col])
            col += 1

        if flag:
            row += 1
        else:
            row -= 1
    return("".join(result))

ciphertext = encrypt(plaintext,key)
decyptedtext = decrypt(ciphertext,key)

print("EncryptedText:",ciphertext)
print("DecryptedText:",decyptedtext)


