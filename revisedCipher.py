plainText = input("Enter the plainText:")

keyTable = [
    'W', 'Q', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'M', 'A', 'S', 'D', 'F', 'G', 'X', 'J', 'K', 'L',"$","%","&", 'Z', 'H', 'C', 'V', 'B', 'N', 'P',
    'w', 'q', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'm', 'a', 's', 'd', 'f', 'g', 'x', 'j', 'k', 'l', 'z', 'h', 'c', 'v', 'b', 'n', 'p'," ","!","@","#"
]
key = 2

def encrypt(plaintext,key):
    ciphertext = ""
    for i in plaintext:
        if i in keyTable: 
            index = keyTable.index(i)
            for j in range(1,key*key+1):
                ciphertext+=keyTable[(index+j*key)%len(keyTable)]
                index+=key
        else:
            ciphertext+=i
            
    return ciphertext
    
def decrypt(ciphertext,key):
    plaintext=""    
    i=0
    while(i<len(ciphertext)):
        if ciphertext[i] in keyTable:
            if i%(key*key) == 0:
                value = ciphertext[i]
                plaintext+=keyTable[(keyTable.index(value)-key)%len(keyTable)]
        else:
            plaintext+=ciphertext[i]
            print(plaintext)
        i+=1

    return plaintext

print("Encrypted Text:", encrypt(plainText,key))
print("Decrypted Text:", decrypt(encrypt(plainText,key),key))