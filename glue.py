from ast import With
import os

arr = os.listdir('output')

print(f"Начинаю склеивание, найдено файлов: {len(arr)}")

for item in arr:
     with open('file', 'ab') as file:
         with open(f'output/{item}', 'rb') as f:
            file.write(f.read())
            print(f"Склеин файл: {item}")

os.rename('fileTEST', 'test.png')

print("Склеивание выполнено!")