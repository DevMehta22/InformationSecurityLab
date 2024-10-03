import math

def caesar_cipher_encrypt_text(text, key):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
        else:
            encrypted_char = char 
        
        encrypted_text += encrypted_char

    return encrypted_text

def caesar_cipher_decrypt_text(encrypted_text, key):
    decrypted_text = ''
    for char in encrypted_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
        else:
            decrypted_char = char
        
        decrypted_text += decrypted_char

    return decrypted_text

def columnar_transposition_encrypt(key, plaintext):
    key_len = len(key)
    num_cols = math.ceil(len(plaintext) / key_len)
    matrix = [[' ' for _ in range(num_cols)] for _ in range(key_len)]
    
    index = 0
    for i in range(num_cols):
        for j in range(key_len):
            if index < len(plaintext):
                matrix[j][i] = plaintext[index]
                index += 1
            else:
                matrix[j][i] = 'X'
    
    key_list = sorted(list(key))
    col_order = [key.index(k) for k in key_list]
    
    ciphertext = ''
    for col in col_order:
        for row in range(num_cols):
            ciphertext += matrix[col][row]
    
    return ciphertext

def columnar_transposition_decrypt(key, ciphertext):
    key_len = len(key)
    num_cols = math.ceil(len(ciphertext) / key_len)
    matrix = [[' ' for _ in range(num_cols)] for _ in range(key_len)]
    
    key_list = sorted(list(key))
    col_order = [key.index(k) for k in key_list]
    
    index = 0
    for col in col_order:
        for row in range(num_cols):
            if index < len(ciphertext):
                matrix[col][row] = ciphertext[index]
                index += 1
    
    plaintext = ''
    for row in range(num_cols):
        for col in range(key_len):
            if matrix[col][row] != 'X':
                plaintext += matrix[col][row]
    
    return plaintext

text = input("Enter the text: ")
key = "GERMAN"
caesar_key = 3 

encrypted_text = caesar_cipher_encrypt_text(text, caesar_key)
encrypted_text = columnar_transposition_encrypt(key, encrypted_text)
print("Encrypted text:", encrypted_text)

decrypted_text = columnar_transposition_decrypt(key, encrypted_text)
decrypted_text = caesar_cipher_decrypt_text(decrypted_text, caesar_key)
print("Decrypted text:", decrypted_text)
