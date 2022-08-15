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
        

        self.select_dir_file.clicked.connect(self.files_dir)
        self.select_pathKey.clicked.connect(self.pathKey)
        self.select_dir_endl.clicked.connect(self.dir_endl)

        self.line_endles_filename.textChanged.connect(self.endles_filename)


        self.start_button_3.clicked.connect(self.glue_start)


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

    def files_dir(self):
        self.line_dir_file.clear()
        filename_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if filename_path:
            self.line_dir_file.setText(filename_path)
    def pathKey(self):
        self.line_pathKey.clear()
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        if filename:
            self.line_pathKey.setText(filename[0])
    def dir_endl(self):
        self.line_dir_endl.clear()
        filename_path = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if filename_path:
            self.line_dir_endl.setText(filename_path)
    def endles_filename(self):
        count_test = self.line_endles_filename.text()
        return count_test

    def glue_start(self):
        path_files = self.line_dir_file.text()
        path_key = self.line_pathKey.text()
        end_filename = self.endles_filename()
        output_dir = self.line_dir_endl.text()

        if path_files:
            self.decryptos(path_files, path_key, end_filename, output_dir)




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

    def decryptos(self, path_files, path_key, end_filename, output_dir):

        with open(path_key, 'rb') as mykey:
            key = mykey.read()
        self.complite_bar.setValue(5)

        f_key = Fernet(key)
        arr = os.listdir(path_files)
        i = 0
        self.complite_bar.setValue(20)
        for item in arr:
            i+=1
            with open(f'{output_dir}/{end_filename}', 'ab') as file:
                with open(f'{path_files}/{item}', 'rb') as f:
                    file.write(f_key.decrypt(f.read()))


        self.complite_bar.setValue(100)




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
