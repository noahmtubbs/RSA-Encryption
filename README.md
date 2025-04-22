# 🔐 RSA Encryption in Python  

What is this?

This is a simple Python program that shows how RSA encryption works behind the scenes. It walks through the whole process: generating keys, encrypting a message, and then decrypting it back. Everything's built from scratch using basic Python and Euler’s totient method — no libraries, no shortcuts.

This project was created as part of a class assignment, but I wanted it to be clean, understandable, and something you could actually learn from.

---

## 🛠️ How It Works

Here’s the basic flow:

1. Generate two random prime numbers (at least 16 bits).
2. Calculate `n = p * q` and `phi(n) = (p - 1)(q - 1)` using Euler’s method.
3. Pick a public key `e` (must be coprime with `phi(n)`).
4. Find the private key `d`, which is the modular inverse of `e` mod `phi(n)`.
5. Read in text from `plaintext.txt`.
6. Encrypt it character by character using the private key.
7. Save the encrypted result to `ciphertext.txt`.
8. Decrypt it back using the public key and save the result to `decoded.txt`.

---

## 🧪 What’s in the Files

| File                | What it’s for 
|---------------------|---------------
| `rsa_encryption.py` | The actual Python script 
| `plaintext.txt`     | The input message (what you want to encrypt) 
| `ciphertext.txt`    | Encrypted output (a list of big numbers) 
| `decoded.txt`       | Decrypted message (should match the original) 
| `README.md`         | This file! 

---

## 💻 How to Run It (Mac/Linux)

1. Put all files in the same folder.
2. Open your Terminal and `cd` into that folder.
3. Run: python3 rsa_encryption.py


