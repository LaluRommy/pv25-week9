from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QFormLayout, QInputDialog
import sys

class Task9(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lalu Rommy Rahmad Amarta Putra - F1D022058")
        self.setGeometry(100, 100, 300, 100)

        layout = QFormLayout()

        self.nama_input = QLineEdit()
        self.nama_input.setReadOnly(True)
        self.nama_input.setPlaceholderText("Nama")
        self.nama_input.mousePressEvent = self.input_name

        self.nim_input = QLineEdit()
        self.nim_input.setReadOnly(True)
        self.nim_input.setPlaceholderText("NIM")
        self.nim_input.mousePressEvent = self.input_nim

        self.bahasa_input = QLineEdit()
        self.bahasa_input.setReadOnly(True)
        self.bahasa_input.setPlaceholderText("Bahasa Pemrograman Favorit")
        self.bahasa_input.mousePressEvent = self.input_language

        layout.addRow("Nama:", self.nama_input)
        layout.addRow("NIM:", self.nim_input)
        layout.addRow("Bahasa Favorit:", self.bahasa_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(layout)

        self.setLayout(main_layout)

    def input_name(self, event):
        text, ok = QInputDialog.getText(self, "Input Nama", "Masukkan nama:")
        if ok and text.strip():
            self.nama_input.setText(text)

    def input_nim(self, event):
        text, ok = QInputDialog.getText(self, "Input NIM", "Masukkan NIM:")
        if ok and text.strip():
            self.nim_input.setText(text)

    def input_language(self, event):
        items = ["Python", "JavaScript", "Java", "C++", "C", "R"]
        item, ok = QInputDialog.getItem(self, "Pilih Bahasa", "Bahasa Favorit:", items, 0, False)
        if ok and item:
            self.bahasa_input.setText(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Task9()
    window.show()
    sys.exit(app.exec_())