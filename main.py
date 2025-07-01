from encriptFIles import encript
import generateKeys
generateKeys.do()
encrypt=encript
folders=["testFolder"]
for folder in folders:
    encrypt.encrypt_files(folder_path=folder)