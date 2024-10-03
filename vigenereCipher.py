plaintext = input("Enter the plain text:")
plaintext=plaintext.upper()
for i in plaintext:
    if i == " ":
        plaintext=plaintext.replace(" ","")
keyword = "VIGENERE"
key = ""
i=0
while(len(key)!=len(plaintext)):
    key += keyword[i]
    i=(i+1)%len(keyword)
    
def encrypt(plaintext,key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isupper():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        else:
            encrypted_char = char
        ciphertext+=encrypted_char
    return ciphertext

def decrypt(ciphertext,key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) +26) % 26 + ord('A'))
        
        else:
            decrypted_char = char
        plaintext+=decrypted_char
    return plaintext
    
    return

print("Encrypted text:",encrypt(plaintext,key))
print("Decrpyted text:",decrypt(encrypt(plaintext,key),key))