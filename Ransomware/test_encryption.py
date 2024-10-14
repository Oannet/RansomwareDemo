import unittest
import secrets
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

from encryption_utils import encrypt_aes_key

class TestEncryption(unittest.TestCase):
    def test_encrypt_aes_key(self):
        aes_key = secrets.token_bytes(32)
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        encrypted_key = encrypt_aes_key(aes_key, public_key)
        self.assertIsNotNone(encrypted_key)

if __name__ == "__main__":
    unittest.main()
