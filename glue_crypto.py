import os
from cryptography.fernet import Fernet

with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

f_key = Fernet(key)

arr = os.listdir('output')

print(f"Начинаю склеивание, найдено файлов: {len(arr)}")

for item in arr:
     with open('fileT', 'ab') as file:
         with open(f'output/{item}', 'rb') as f:
            file.write(f_key.decrypt(f.read()))
            print(f"Склеин файл: {item}")

os.rename('fileT', 'test1.png')

print("Склеивание выполнено!")