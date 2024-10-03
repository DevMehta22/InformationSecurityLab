def rsa_secrets():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    d = pow(e, -1, phi)
    
    public_key = [e,n]
    private_key = [d,n]
    
    return private_key,public_key

def encryption(plaintext,public_key):
    encrypted_text = [(ord(char)**public_key[0])%public_key[1] for char in plaintext]
    return encrypted_text

def decryption(ciphertext,private_key):
    decrypted_text = ''.join([chr((char ** private_key[0]) % private_key[1]) for char in ciphertext])
    return decrypted_text

plaintext = "HELLOWORLD"
public_key,private_key = rsa_secrets()
ciphertext = encryption(plaintext,public_key)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decryption(ciphertext,private_key))
    

    
