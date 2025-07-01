from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

class encript:
    def __init__(self):
        self.AES_key = None  #

    def load_key(self):
        private_key = RSA.import_key(open("private.pem").read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        with open("encrypted_key.bin", "rb") as f:
            encrypted_key = f.read()
        self.AES_key = cipher_rsa.decrypt(encrypted_key)

    def decrypt_files(self, folder_path):
        try:
            self.load_key()
            file_list = os.listdir(folder_path)
            for filename in file_list:
                if not filename.endswith(".enc"):
                    continue
                path = os.path.join(folder_path, filename)
                with open(path, "rb") as f:
                    nonce = f.read(16)
                    tag = f.read(16)
                    ciphertext = f.read()
                cipher = AES.new(self.AES_key, AES.MODE_GCM, nonce=nonce)
                data = cipher.decrypt_and_verify(ciphertext, tag)

                original_path = path[:-4]
                with open(original_path, "wb") as f:
                    f.write(data)
                os.remove(path)
            print("✅ Decryption completed")
            return True
        except Exception as e:
            print(f"⛔ Error during decryption: {e}")
            return False
