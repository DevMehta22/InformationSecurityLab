import random

def generate_playfair_matrix(key):
    all_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789[]"
    matrix = []

    shuffled_chars = list(all_chars)
    random.shuffle(shuffled_chars)

    for char in key:
        if char not in matrix:
            matrix.append(char)

    for char in shuffled_chars:
        if char not in matrix:
            matrix.append(char)
        if len(matrix) == 64: 
            break
    
    return [matrix[i:i+8] for i in range(0, 64, 8)]


def find_position(char, matrix):
    for row in range(8):
        for col in range(8):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    if row1 == row2 and row1%2==0:
        return matrix[row1][(col1 + 1) % 8] + matrix[row2][(col2 + 1) % 8]
    elif row1 == row2 and row1%2!=0:
        return matrix[row1][(col1 - 1) % 8] + matrix[row2][(col2 - 1) % 8]
    elif col1 == col2 and col1%2==0:
        return matrix[(row1 + 1) % 8][col1] + matrix[(row2 + 1) % 8][col2]
    elif col1 == col2 and col1%2!=0:
        return matrix[(row1 - 1) % 8][col1] + matrix[(row2 - 1) % 8][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(pair, matrix):
    row1, col1 = find_position(pair[0], matrix)
    row2, col2 = find_position(pair[1], matrix)

    if row1 == row2 and row1%2==0:
        return matrix[row1][(col1 - 1) % 8] + matrix[row2][(col2 - 1) % 8]
    elif row1 == row2 and row1%2!=0:
        return matrix[row1][(col1 + 1) % 8] + matrix[row2][(col2 + 1) % 8]
    elif col1 == col2 and col1%2==0:
        return matrix[(row1 - 1) % 8][col1] + matrix[(row2 - 1) % 8][col2]
    elif col1 == col2 and col1%2!=0:
        return matrix[(row1 + 1) % 8][col1] + matrix[(row2 + 1) % 8][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def prepare_text(text):
    for i in text:
        if i == ' ':
            text = text.replace(' ', '')
    prepared = ''
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared += text[i] + 'X' 
            i += 1
        elif text[i] == text[i + 1]:
            prepared += text[i] + 'X'
            i += 1
        else:
            prepared += text[i] + text[i + 1]
            i += 2
    return prepared

def encrypt_text(plaintext, matrix):
    prepared_text = prepare_text(plaintext)
    ciphertext = ''
    for i in range(0, len(prepared_text), 2):
        ciphertext += encrypt_pair(prepared_text[i:i+2], matrix)
    return ciphertext

def decrypt_text(ciphertext, matrix):
    decrypted_text = ''
    for i in range(0, len(ciphertext), 2):
        decrypted_text += decrypt_pair(ciphertext[i:i+2], matrix)
    return decrypted_text.replace('X', '')


key = "keyWordQQ"
matrix = generate_playfair_matrix(key)


plaintext = input("Enter the plaintext: ")
ciphertext = encrypt_text(plaintext, matrix)
print("Encrypted text:", ciphertext)


decrypted_text = decrypt_text(ciphertext, matrix)
print("Decrypted text:", decrypted_text)

