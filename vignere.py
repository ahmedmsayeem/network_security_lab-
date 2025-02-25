def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ""
    key_index = 0
    for char in ciphertext.upper():
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            plaintext += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char
    return plaintext

# Example usage
plaintext = "HELLO"
key = "KEY"
encrypted = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
