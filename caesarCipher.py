plainText = input("Enter the text:")
key = 5

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext,key):
    cipherText = ""
    for i in plaintext:
        if i in uppercase:
            cipherText += uppercase[(uppercase.index(i) + key) % 26]
        elif i in lowercase:
            cipherText += lowercase[(lowercase.index(i) + key) % 26]
        else:
            cipherText += i
    return cipherText


cipherText = encrypt(plainText,key)

def decrypt(ciphertext,key):
    decryptedText = ""
    for i in ciphertext:
        if i in uppercase:
            decryptedText += uppercase[(uppercase.index(i) - key) % 26]
        elif i in lowercase:
            decryptedText += lowercase[(lowercase.index(i) - key) % 26]
        else:
            decryptedText += i   
    return decryptedText
 
decryptedText = decrypt(cipherText,key)

print("Encrypted Text:",cipherText)
print("Decrypted Text:",decryptedText)