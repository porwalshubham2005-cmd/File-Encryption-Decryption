# 🔐 File Encryption & Decryption

A simple Python-based file encryption and decryption tool using the **Caesar Cipher algorithm**.

This project allows users to:
- Encrypt text files
- Save encrypted content into a new file
- Decrypt encrypted files
- Restore the original content using the correct encryption key

## 🚀 Features

- Simple command-line interface
- File encryption using Caesar Cipher
- File decryption using the same key
- Creates separate encrypted and decrypted files
- Handles missing files and invalid inputs
- No external Python libraries required

## 🛠️ Technologies Used

- Python 3
- File Handling
- Caesar Cipher
- Command Line Interface

## 📁 Project Structure

```text
File-Encryption-Decryption/
│
├── file_encryption.py
├── requirements.txt
├── README.md
├── .gitignore
├── sample.txt
└── screenshots/
```

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/porwalshubham2005-cmd/File-Encryption-Decryption.git
```

### 2. Open the project folder

```bash
cd File-Encryption-Decryption
```

### 3. Run the program

```bash
python file_encryption.py
```

## 🔒 Encrypt a File

Select:

```text
1. Encrypt File
```

Then enter the file name and encryption key.

Example:

```text
Enter your choice (1/2): 1
Enter file path: sample.txt
Enter encryption key (1-25): 3
```

Output:

```text
File encrypted successfully!
Encrypted file: sample_encrypted.txt
```

## 🔓 Decrypt a File

Run the program again and select:

```text
2. Decrypt File
```

Example:

```text
Enter your choice (1/2): 2
Enter file path: sample_encrypted.txt
Enter encryption key (1-25): 3
```

The program creates:

```text
sample_encrypted_decrypted.txt
```

The decrypted file contains the original text.

## 🔑 How Caesar Cipher Works

The Caesar Cipher shifts each alphabetic character by a fixed number of positions.

For example, with key `3`:

```text
A → D
B → E
C → F
```

So:

```text
Hello
```

becomes:

```text
Khoor
```

Using the same key during decryption restores:

```text
Khoor → Hello
```

## ⚠️ Important

The same encryption key must be used during decryption.

Example:

```text
Encryption Key: 3
Decryption Key: 3
```

## 📦 Requirements

This project uses only Python's built-in libraries.

No external packages are required.

## 🎯 Internship Task

This project was developed as part of the **Codveda Technologies Python Development Internship**.

### Task Objective

- Implement basic file encryption and decryption
- Allow users to select files
- Save encrypted content into a new file
- Decrypt the encrypted file back to its original form

## 👨‍💻 Author

**Shubham Porwal**

GitHub:  
https://github.com/porwalshubham2005-cmd
