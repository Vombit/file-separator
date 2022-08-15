import os
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import os

import math
from cryptography.fernet import Fernet

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.select_end_dir.clicked.connect(self.output_folder)
        self.select_filename.clicked.connect(self.first_file)

        self.select_count_chunks.valueChanged.connect(self.couts_chunks)

        self.select_count_size.textChanged.connect(self.couts_size)
            

        self.start_chunks_split.clicked.connect(self.start_chunk_split)
        self.start_size_split.clicked.connect(self.start_size_splits)
        
    def output_folder(self):
        self.line_end_dir.clear()
        filename_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if filename_path:
            self.line_end_dir.setText(filename_path)
    def first_file(self):
        self.line_filename.clear()
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        
        if filename:
            self.line_filename.setText(filename[0])

    def couts_chunks(self):
        count_test = self.select_count_chunks.value()

        return count_test

    def couts_size(self):
        count_test = self.select_count_size.text()
        return count_test

    def start_chunk_split(self):
        name_filename = self.line_filename.text()
        name_uot = self.line_end_dir.text()
        name_chunk = self.couts_chunks()

        if name_filename:
            self.cryptos(name_uot, name_filename, name_chunk, 0)

    def start_size_splits(self):
        name_filename = self.line_filename.text()
        name_uot = self.line_end_dir.text()
        name_chunk = int(self.couts_size())

        if name_filename:
            self.cryptos(name_uot, name_filename, name_chunk, 1)


    def cryptos(self, path_out, file_name, chunk_count, mode):
        key = Fernet.generate_key()
        with open('mykey.key', 'wb') as mykey:
            mykey.write(key)
        f_key = Fernet(key)
        self.complite_bar.setValue(5)

        filename = file_name
        chunks = chunk_count
        
        file_size = 0
        with open(filename, "rb") as frb:
            for line in frb:
                file_size += len(line)

        if mode == 0:
            chunks_size = math.ceil(file_size/chunks)
            self.complite_bar.setValue(10)

            with open(filename, "rb") as fr:
                i = 0
                while i < chunks:
                    i+=1
                    self.complite_bar.setValue(int(100/chunks*i))
                    with open(f'{path_out}/{i}', 'wb') as f:
                        f.write(f_key.encrypt(fr.read(chunks_size)))
        else:
            chunks_size = chunks*1024*768

            all_cnk_cnt = math.ceil(file_size/chunks_size)
            self.complite_bar.setValue(10)

            with open(filename, "rb") as fr:
                i = 0
                while i < all_cnk_cnt:
                    i+=1
                    self.complite_bar.setValue(int(100/all_cnk_cnt*i))
                    with open(f'{path_out}/{i}', 'wb') as f:
                        f.write(f_key.encrypt(fr.read(chunks_size)))

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
