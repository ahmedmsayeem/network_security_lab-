import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    
    d = mod_inverse(e, phi)
    if d is None:
        raise ValueError("Could not find modular inverse for e.")
    
    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    encrypted_msg = [pow(ord(char), e, n) for char in message]
    return encrypted_msg

def decrypt(encrypted_msg, private_key):
    d, n = private_key
    decrypted_msg = ''.join([chr(pow(char, d, n)) for char in encrypted_msg])
    return decrypted_msg

if __name__ == "__main__":
    p = 61  # First prime number
    q = 53  # Second prime number
    
    public_key, private_key = generate_keys(p, q)
    print("Public Key:", public_key)
    print("Private Key:", private_key)
    
    message = "HELLO"
    encrypted_msg = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_msg)
    
    decrypted_msg = decrypt(encrypted_msg, private_key)
    print("Decrypted Message:", decrypted_msg)
