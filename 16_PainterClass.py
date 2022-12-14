from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter,QPen,QBrush
from PyQt5.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 PainterClass")
        self.setGeometry(500, 200, 500, 400)

    def paintEvent(self,e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.yellow,5,Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green,Qt.BrushStyle.DiagCrossPattern))
        painter.drawRect(100,15,300,100)



app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
