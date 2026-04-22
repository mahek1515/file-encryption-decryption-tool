# Secure File Encryption & Decryption System

This project is a secure file encryption and decryption application developed using Python and Streamlit. It enables users to protect sensitive files through encryption and restore them באמצעות decryption using a generated secret key.

The system uses **Fernet symmetric encryption** from the cryptography library, ensuring strong and reliable data protection.

## Key Features

- Secure file encryption using Fernet (symmetric cryptography)
- File decryption with user-provided secret key
- Automatic secret key generation
- Interactive web interface using Streamlit
- Secure in-memory handling using session state
- Downloadable encryption key and decrypted files

## How It Works

1. Upload a file to encrypt
2. System generates a secure encryption key
3. File is encrypted and stored temporarily
4. Download the secret key
5. Upload the key to decrypt the file
6. Download the original decrypted file

## Technologies Used

- Python
- Streamlit
- Cryptography (Fernet)

## Security Note

- The secret key is required to decrypt the file
- If the key is lost, the encrypted data cannot be recovered
- This system uses symmetric encryption, meaning the same key is used for encryption and decryption
