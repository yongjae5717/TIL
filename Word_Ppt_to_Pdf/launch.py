from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtCore import Qt
import os
import comtypes.client


class MyGUI(QMainWindow):

    def __init__(self):
        self.word_dir_path = ""
        self.ppt_dir_path = ""
        self.pdf_dir_path = ""
        super(MyGUI, self).__init__()
        uic.loadUi("word_ppt_to_pdf.ui", self)

    def resizeEvent(self, event):
        self.pushButton_1.clicked.connect(self.open_directory)
        self.pushButton_2.clicked.connect(self.open_directory2)
        self.pushButton_3.clicked.connect(self.open_directory3)
        self.pushButton_4.clicked.connect(self.word_to_pdf)
        self.pushButton_5.clicked.connect(self.ppt_to_pdf)

    def ppt_to_pdf(self):
        input_folder_path = self.ppt_dir_path.replace('/', "\\")
        output_folder_path = self.pdf_dir_path.replace('/', "\\")
        print(input_folder_path, output_folder_path)
        input_file_paths = os.listdir(input_folder_path)

        for input_file_name in input_file_paths:

            if not input_file_name.lower().endswith((".ppt", ".pptx")):
                continue
            input_file_path = os.path.join(input_folder_path, input_file_name)

            powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
            powerpoint.Visible = True
            slides = powerpoint.Presentations.Open(input_file_path)
            file_name = os.path.splitext(input_file_name)[0]
            output_file_path = output_folder_path + "/" + file_name + ".pdf"
            output_file_path = output_file_path.replace("/", "//")
            print("break point", output_file_path)
            slides.SaveAs(output_file_path, FileFormat=32)
            print("break point")
            slides.Close()

    def word_to_pdf(self):
        input_folder_path = self.word_dir_path.replace('/', "\\")
        output_folder_path = self.pdf_dir_path.replace('/', "\\")
        input_file_paths = os.listdir(input_folder_path)

        for input_file_name in input_file_paths:

            if not input_file_name.lower().endswith((".doc", ".docx")):
                continue

            input_file_path = os.path.join(input_folder_path, input_file_name)

            word = comtypes.client.CreateObject('Word.Application')
            word.Visible = True
            doc = word.Documents.Open(input_file_path)

            file_name = os.path.splitext(input_file_name)[0]
            output_file_path = os.path.join(output_folder_path, file_name + ".pdf")

            doc.SaveAs(output_file_path, FileFormat=17)
            doc.Close()

    def open_directory(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if directory == "":
            QMessageBox.warning(self, "Error", "폴더 선택이 되지 않았습니다.")
            return
        self.label_1.setText(directory)
        self.word_dir_path = directory

    def open_directory2(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if directory == "":
            QMessageBox.warning(self, "Error", "폴더 선택이 되지 않았습니다.")
            return
        self.label_2.setText(directory)
        self.ppt_dir_path = directory

    def open_directory3(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if directory == "":
            QMessageBox.warning(self, "Error", "폴더 선택이 되지 않았습니다.")
            return
        self.label_3.setText(directory)
        self.pdf_dir_path = directory


def main():
    app = QApplication([])
    window = MyGUI()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()