from Crypto.Cipher import DES
from secrets import token_bytes
import time

def encrypt(password):
    start = time.perf_counter()

    key = token_bytes(8)

    cipher = DES.new(key, DES.MODE_EAX)

    nonce = cipher.nonce

    encrypted_password = cipher.encrypt(password.encode('utf-8'))
    
    end = time.perf_counter()

    return key, nonce, encrypted_password, ((end-start)*1000.0)


def decrypt(encrypted_password, key, nonce):
    start = time.perf_counter()

    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)

    decrypted_password = cipher.decrypt(encrypted_password)

    end = time.perf_counter()

    return decrypted_password, ((end-start)*1000.0)

