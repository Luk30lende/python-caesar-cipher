# Caesar Cipher (Python)

A Python implementation of the **Caesar Cipher**, one of the simplest and most well-known encryption techniques. This project supports both encryption and decryption, preserves letter casing, and validates user input.

Built as part of the **freeCodeCamp Python code challenge**.

---

## 📌 What is a Caesar Cipher?

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet.

**Example (shift = 3):**
- A → D  
- B → E  
- C → F  

The same logic applies in reverse for decryption.

---

## 🚀 Features

- Encrypt and decrypt text using a shift value
- Preserves uppercase and lowercase letters
- Ignores non-alphabetic characters (numbers, spaces, symbols)
- Input validation for shift values
- Clean, reusable function-based design

---

## 🛠️ How It Works

The program:
1. Defines the alphabet
2. Shifts the alphabet by the given number
3. Uses `str.maketrans()` and `translate()` to map characters efficiently
4. Reverses the shift automatically when decrypting

---

## 📄 Code Example

```python
encrypted_text = encrypt('freeCodeCamp', 3)
print(encrypted_text)
```

## Output:
iuhhFrghFdps

## 📚 Learning Objectives

This project demonstrates:
- Python string manipulation
- Alphabet shifting with slicing
- Use of str.maketrans() and translate()
- Clean function design
- Basic cryptography concepts

 ## 👨‍💻 Author

Luke Olende
Built as part of the freeCodeCamp Python curriculum.
