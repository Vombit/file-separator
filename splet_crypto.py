import math
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

f_key = Fernet(key)

filename = "test.png"
chunks = 10

file_size = 0
with open(filename, "rb") as frb:
    for line in frb:
        file_size += len(line)
chunks_size = math.ceil(file_size/chunks)
print(f"Размер чанка: {chunks_size/1024} килобайт")

with open(filename, "rb") as fr:
    i = 0
    while i < chunks:
        with open(f'output/{i}', 'wb') as f:
            f.write(f_key.encrypt(fr.read(chunks_size)))
        i+=1
        print("Готов чанк:", i)


print("Файл поделён!")
