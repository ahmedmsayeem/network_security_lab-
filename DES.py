import random
from Crypto.Cipher import DES

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def generate_key():
    return ''.join(chr(random.randint(0, 255)) for _ in range(8)).encode('utf-8')

def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return encrypted_text

def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decrypted_text = des.decrypt(encrypted_text).decode('utf-8').strip()
    return decrypted_text

if __name__ == "__main__":
    key = generate_key()
    print("Generated Key:", key)
    
    message = input("Enter a message: ")
    encrypted_msg = encrypt(message, key)
    print("Encrypted Message:", encrypted_msg)
    
    decrypted_msg = decrypt(encrypted_msg, key)
    print("Decrypted Message:", decrypted_msg)
