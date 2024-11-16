def encrypt(plaintext,key):
    ciphertext = ""
    j=0
    for i in plaintext:
        if(i.isalpha()):
            ciphertext+=chr(ord(i)+key[j])
            j+=1
            if(j==len(key)):
                j=0
    
    return ciphertext

def decrypt(ciphertext,key,filler_len):
    plaintext = ""
    j = 0
    for i in ciphertext:
        if(i.isalpha()):
            plaintext+=chr(ord(i)-key[j])
            j+=1
            if(j==len(key)):
                j=0
                
    plaintext = list(plaintext)
    
    while(filler_len>0): 
        plaintext.pop()
        filler_len-=1
    
    return "".join(plaintext)

plain_text = input("Enter the plain text:")
min_letter = input("Enter the minimum letter:")
plain_text = plain_text.upper()
min_letter = min_letter.upper()

key = int(input("Enter the key:"))
key = [int(x) for x in str(key)]
filler_len = len(key)-len(plain_text)%len(key)

if(len(plain_text)%len(key)!=0):
    plain_text += min_letter.upper() * filler_len

cipher_text = encrypt(plain_text,key)
print("Encrypted Text:"+cipher_text)
print("Decrypted Text:"+decrypt(cipher_text,key,filler_len))
