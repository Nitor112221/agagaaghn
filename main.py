import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import random


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.circle)

    def circle(self):
        self.draw = True
        self.update()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawing(qp)
            qp.end()
            self.draw = False

    def drawing(self, qp):
        qp.setBrush(QColor('Yellow'))
        d = random.randint(50, 100)
        qp.drawEllipse((400 - d) // 2, (400 - d) // 2, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
