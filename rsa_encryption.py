# RSA Encryption and Decryption in Python
# Author: Noah Tubbs
# Description:
#   - Generates RSA public/private keys (with at least 16-bit primes)
#   - Encrypts a message from 'plaintext.txt' using the private key
#   - Decrypts the message using the public key
#   - Saves encrypted data to 'ciphertext.txt' and decrypted text to 'decoded.txt'

import random
from math import gcd
from pathlib import Path

# Prime Checking and Generation
def is_prime(n):
     # Checks if n is a prime number
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime(bits=16):
    # Generates a random prime number with at least 'bits' binary length
    while True:
        p = random.getrandbits(bits)
        if is_prime(p):
            return p

# Modular Inverse (used for private key)
def modinv(a, m):
    # Extended Euclidean Algorithm to find modular inverse of a mod m
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# RSA Key Generation
def generate_keys():
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    # Commonly used public exponent
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Private exponent
    d = modinv(e, phi)
    return ((e, n), (d, n))

# RSA Encryption and Decryption
def encrypt(text, key):
    # Encrypts plaintext character-by-character using RSA private key
    d, n = key
    return [pow(ord(char), d, n) for char in text]

def decrypt(cipher, key):
    # Decrypts ciphertext using RSA public key
    e, n = key
    return ''.join([chr(pow(c, e, n)) for c in cipher])

# File I/O Helpers
def read_plaintext(file_path):
    return Path(file_path).read_text()

def write_ciphertext(cipher, file_path):
    with open(file_path, 'w') as f:
        f.write(' '.join(map(str, cipher)))

def read_ciphertext(file_path):
    with open(file_path, 'r') as f:
        return list(map(int, f.read().split()))

def write_decoded(text, file_path):
    Path(file_path).write_text(text)


# Main
def main():
    plaintext_file = 'plaintext.txt'
    ciphertext_file = 'ciphertext.txt'
    decoded_file = 'decoded.txt'

    # Generate RSA keys
    public_key, private_key = generate_keys()

    # Read input message
    plaintext = read_plaintext(plaintext_file)

    # Encrypt the message with the private key
    cipher = encrypt(plaintext, private_key)
    write_ciphertext(cipher, ciphertext_file)

    # Decrypt using the public key
    loaded_cipher = read_ciphertext(ciphertext_file)
    decoded = decrypt(loaded_cipher, public_key)
    write_decoded(decoded, decoded_file)

    # Print results for demo
    print("RSA Encryption/Decryption complete.\n")
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

if __name__ == '__main__':
    main()
