import hashlib

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

def encrypt(text,private_key):
    d = private_key[0]
    n = private_key[1]
    encrypted_text = [(ord(char)**d)%n for char in text]
    return encrypted_text

def decrypt(text,public_key):
    e = public_key[0]
    n = public_key[1]
    decrypted_text = ''.join([chr((char**e)%n) for char in text])
    return decrypted_text
    
plaintext = input("Enter the Plain text:")

msg_digest = (hashlib.sha1(plaintext.encode())).hexdigest()
print("Message_digest(sender):",msg_digest)

private_key,public_key = rsa_secrets()

signature_list = encrypt(msg_digest,private_key)
print(signature_list)

final_msg = plaintext+"$"+str(signature_list)

print("Final Mesaage from sender(A):", final_msg)


msg_list = final_msg.split("$")
print(msg_list)

received_plaintext = msg_list[0]
received_signature_list = eval(msg_list[1])

msg_digest_2 = decrypt(received_signature_list,public_key)
print(msg_digest_2)

msg_digest_3 = (hashlib.sha1(received_plaintext.encode())).hexdigest()
print(msg_digest_3)

if msg_digest_2 == msg_digest_3:
    print("Signature is valid")
else:
    print("Signature is invalid")



