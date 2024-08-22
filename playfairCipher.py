plain_text = input("Enter the Plain text:")
key = "KEYWORD"
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
space_list=[]
j_list = []
double_list = []

Matrix = []

for k in key:
    if k not in Matrix:
        Matrix.append(k)
        
for letter in alphabet:
    if letter not in Matrix:
        Matrix.append(letter)

playfair_matrix = [Matrix[i:i + 5] for i in range(0, len(Matrix), 5)]

# print(playfair_matrix)

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def encrypt(plain_text, matrix):
    for i in range(len(plain_text)):
        
        if (plain_text[i] == "J"):
            j_list.append(i)
        
        if (plain_text[i] == " "):
            space_list.append(i)
            
    
    for i in range(len(plain_text)-1):
        if (plain_text[i]==plain_text[i+1]):
            double_list.append(i)
            plain_text = plain_text[:i] + "X" + plain_text[i+1:]
        
        if (plain_text[i]=="X" and plain_text[i+1]== "X"):
            double_list.append(i)
            plain_text = plain_text[:i] + "Z" + plain_text[i+1:] 
            
    
    plain_text = plain_text.upper().replace("J", "I")
    plain_text = plain_text.upper().replace(" ", "")

    if len(plain_text) % 2 != 0:
        plain_text += "Z"

    cipher_text = ""

    print(j_list)
    print(space_list)
    
    i = 0
    while i < len(plain_text):
        a = plain_text[i]
        b = plain_text[i + 1]
           
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            cipher_text += matrix[row1][(col1 + 1) % 5]
            cipher_text += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            cipher_text += matrix[(row1 + 1) % 5][col1]
            cipher_text += matrix[(row2 + 1) % 5][col2]
        else:

            cipher_text += matrix[row1][col2]
            cipher_text += matrix[row2][col1]

        i += 2
        
    
    return cipher_text

def decrypt(ciphertext,matrix):
    plaintext=""
    i=0
    while i<len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1]
        row1,col1 = find_position(matrix,a)
        row2,col2 = find_position(matrix,b)
        
        if row1 == row2:
            plaintext+=matrix[row1][(col1-1)%5]
            plaintext+=matrix[row2][(col2-1)%5]
        
        elif col1 == col2:
            plaintext+=matrix[(row1-1)%5][col1]
            plaintext+=matrix[(row2-1)%5][col2]
            
        else:
            plaintext+=matrix[row1][col2]
            plaintext+=matrix[row2][col1]
    
        i+=2
        
    for index in space_list:
        plaintext = plaintext[:index] + " " + plaintext[index:]

    for index in j_list:
        plaintext = plaintext[:index] + "J" + plaintext[index + 1:]
    
    for index in double_list:
        plaintext = plaintext[:index] + plaintext[index+1] + plaintext[index + 1:]
    
    if (plain_text[-1]!= plaintext[-1]):
        plaintext = plaintext[:-1]

    return plaintext

cipher_text=encrypt(plain_text,playfair_matrix)
print(cipher_text)
print(decrypt(cipher_text,playfair_matrix))

    



