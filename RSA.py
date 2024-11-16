import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_e(phi):
    e = 3
    while gcd(e, phi) != 1:
        e += 2  
    return e

def rsa_secrets():
    p = int(input("Enter p:"))
    q = int(input("Enter q:"))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_e(phi)
    d = pow(e, -1, phi)
    
    public_key = [e, n]
    private_key = [d, n]
    
    return private_key, public_key

def encryption(plaintext, public_key):
    e = public_key[0]
    n = public_key[1]
    encrypted_text = [(ord(char)**e) % n for char in plaintext]
    return encrypted_text

def decryption(ciphertext, private_key):
    d = private_key[0]
    n = private_key[1]
    decrypted_text = ''.join([chr((char ** d) % n) for char in ciphertext])
    return decrypted_text

public_key, private_key = rsa_secrets()
plaintext = input("Enter the plaintext: ")
ciphertext = encryption(plaintext, public_key)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decryption(ciphertext, private_key))
