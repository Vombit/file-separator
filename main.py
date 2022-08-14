import os
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
import os
class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.select_end_dir.clicked.connect(self.output_folder)
        self.select_filename.clicked.connect(self.first_file)
        
        self.select_count_chunks.valueChanged.connect(self.couts_chunks)

        self.start_chunks_split.clicked.connect(self.start_chunk_split)
        




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

    def start_chunk_split(self):
        print(self.line_filename.text())
        print(self.line_end_dir.text())
        print(self.couts_chunks())




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
