def encrypt(plaintext):
    word_count = 1
    letter_count = 0
    ciphertext = ""
    key = []
   
    for i in plaintext:
        if (i != " "):
            val = word_count + letter_count
            key.append(val)
            ciphertext+=chr((ord(i) - ord("A") + val)%26 + ord("A"))
            
            letter_count += 1
        else:
            key.append(" ")
            ciphertext+=" "
            word_count += 1
            letter_count = 0
            
    return ciphertext,key

def decrypt(ciphertext,key):
    plaintext = ""
    key_index = 0

    for i in range(len(ciphertext)):
        if ciphertext[i] == " ":
            plaintext += " "
            key_index += 1
            continue

        val = key[key_index]
        if(val!=" "):
            plaintext += chr(((ord(ciphertext[i]) - ord('A') - val) % 26) + ord('A'))
        
        key_index += 1
    
    return plaintext
    
plain_text = input("Enter the plain text:")
plain_text = plain_text.upper()

cipher_text,key = encrypt(plain_text)
print("Key:"+"".join(str(key)))
print("Cipher Text:"+cipher_text) 
print("Decrypted Text:"+decrypt(cipher_text,key))
