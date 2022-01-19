from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import time

def encrypt(password):
    start = time.perf_counter()

    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            break
        except ValueError:
            pass

    cipher = DES3.new(key, DES3.MODE_EAX)

    nonce = cipher.nonce

    encrypted_password = cipher.encrypt(password.encode('utf-8'))
    
    end = time.perf_counter()

    return key, nonce, encrypted_password, ((end-start)*1000.0)


def decrypt(encrypted_password, key, nonce):
    start = time.perf_counter()

    cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)

    decrypted_password = cipher.decrypt(encrypted_password)

    end = time.perf_counter()

    return decrypted_password, ((end-start)*1000.0)
            
