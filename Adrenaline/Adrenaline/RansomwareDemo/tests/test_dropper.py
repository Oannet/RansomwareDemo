import unittest
import os
import sys

# Añade la ruta a src/dropper
sys.path.insert(0, os.path.abspath('../src/dropper'))

from dropper import download_file, install_dependencies

class TestDropper(unittest.TestCase):
    def test_download_file(self):
        # Prueba para copiar un archivo local en lugar de descargarlo
        src = os.path.abspath("../src/main/main.py")
        dest = "test_main.py"
        download_file(src, dest)
        self.assertTrue(os.path.exists(dest))
        os.remove(dest)  # Limpieza después de la prueba
    
    def test_install_dependencies(self):
        result = install_dependencies()
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()
