import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser


class Suffle(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 265, 45)
        self.setWindowTitle('Фокус со словами')

        self.text_field = QTextBrowser(self)
        self.text_field.resize(100, 25)
        self.text_field.move(5, 100)

        self.button = QPushButton('Загрузить строки', self)
        self.button.resize(25, 15)
        self.button.move(5, 20)
        self.button.clicked.connect(self.cl)

    def cl(self):
        f = open("lines.txt", mode="r", encoding="utf8")
        d = []
        d1 = []
        s = 0
        for i in list(f):
            if s % 2 == 0 or s == 0:
                d.append(i.strip())
            else:
                d1.append(i.strip())
            s += 1
        d1.extend(d)
        s = ''
        for i in d1:
            s += i + '\n'
        self.text_field.setPlainText(s)
        f.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suffle()
    ex.show()
    sys.exit(app.exec())
