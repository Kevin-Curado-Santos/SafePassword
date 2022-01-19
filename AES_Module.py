from Crypto.Cipher import AES 
from Crypto.Random import get_random_bytes
import time

def encrypt(password):
    start = time.perf_counter() 

    key = get_random_bytes(16) # random 16 bytes key
   
    cipher = AES.new(key, AES.MODE_EAX) 

    nonce = cipher.nonce

    password = password.encode('utf-8')

    encrypted_password = cipher.encrypt(password) # encrypts the password

    end = time.perf_counter()
    
    return key, nonce, encrypted_password, ((end-start)*1000.0)


def decrypt(encrypted_password, key, nonce):
    start = time.perf_counter()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    decrypted_password = cipher.decrypt(encrypted_password)
    
    end = time.perf_counter()

    return decrypted_password, ((end-start)*1000.0)

