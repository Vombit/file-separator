import math

filename = "test.png"
chunks = 4

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
            f.write(fr.read(chunks_size))
        i+=1
        print("Готов чанк:", i)


print("Файл поделён!")