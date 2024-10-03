def char_to_num(char):
    return ord(char) - 32  

def num_to_char(num):
    return chr(num + 32)   

def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        p_num = char_to_num(plaintext[i]) 
        k_num = char_to_num(key[i])        
        encrypted_num = (p_num + k_num) % 95  
        ciphertext += num_to_char(encrypted_num)  
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        c_num = char_to_num(ciphertext[i])  
        k_num = char_to_num(key[i])         
        decrypted_num = (c_num - k_num + 95) % 95  
        plaintext += num_to_char(decrypted_num)    
    return plaintext

plaintext = input("Enter the plain text: ")
keyword = "VIGENERE"
key = ""

i=0
while(len(key)!=len(plaintext)):
    key += keyword[i]
    i=(i+1)%len(keyword)

ciphertext = encrypt(plaintext, key)
print("Encrypted text:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
