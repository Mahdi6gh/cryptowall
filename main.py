from encriptFIles import encript
import generateKeys
generateKeys.do()
encrypt=encript
encrypt.encrypt_files(folder_path="testFolder")