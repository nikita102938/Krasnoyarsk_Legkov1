from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPainter, QColor, QPolygon
import sys
import random
from UI import Ui_MainWindow

SCREEN_SIZE = [680, 480]


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fl = False
        self.setWindowTitle('пусто')
        self.pushButton.clicked.connect(self.draw)
        self.crd = []

    def draw(self):
        self.fg = 'circle'
        self.size = random.randint(10, 100)
        self.color = (255, 255, 0)  # 'yellow'
        self.fl = True
        self.update()

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(*self.color))
            qp.setBrush(QColor(*self.color))
            self.x, self.y = 200, 200
            if self.fg == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec())