def generate_key_matrix(key):
    key = "".join(sorted(set(key), key=key.index))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []

    for char in key:
        if char not in matrix:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    matrix_5x5 = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return matrix_5x5

def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    processed_text = ""

    i = 0
    while i < len(text):
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += 'X'
        elif i + 1 < len(text):
            processed_text += text[i + 1]
            i += 1
        i += 1

    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    
    return processed_text

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_digraph(digraph, matrix):
    row1, col1 = find_position(digraph[0], matrix)
    row2, col2 = find_position(digraph[1], matrix)

    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_digraph(digraph, matrix):
    row1, col1 = find_position(digraph[0], matrix)
    row2, col2 = find_position(digraph[1], matrix)

    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_cipher(text, key, mode='encrypt'):
    matrix = generate_key_matrix(key)
    processed_text = preprocess_text(text)
    output = ""

    for i in range(0, len(processed_text), 2):
        digraph = processed_text[i:i+2]
        if mode == 'encrypt':
            output += encrypt_digraph(digraph, matrix)
        elif mode == 'decrypt':
            output += decrypt_digraph(digraph, matrix)
    
    return output

# Example usage:
key = "KEYWORD"
text = "HELLO WORLD"

encrypted_text = playfair_cipher(text, key, mode='encrypt')
print("Encrypted Text:", encrypted_text)

decrypted_text = playfair_cipher(encrypted_text, key, mode='decrypt')
print("Decrypted Text:", decrypted_text)
