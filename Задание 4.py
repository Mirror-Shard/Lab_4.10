import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt, QPoint


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(500, 500)
        canvas.fill(Qt.white)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    def draw_something(self):
        canvas = self.label.pixmap()
        painter = QtGui.QPainter(canvas)
        pen = QtGui.QPen()
        pen.setWidth(3)

        pen.setColor(QtGui.QColor('Lightblue'))
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('Lightblue'))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        painter.drawPolygon(QtGui.QPolygon([
            QPoint(250, 120),
            QPoint(385, 200),
            QPoint(115, 200),
        ]))
        painter.drawRect(150, 200, 200, 200)

        pen.setColor(QtGui.QColor('orange'))
        painter.setPen(pen)
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('orange'))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawEllipse(400, 10, 80, 80)

        pen.setColor(QtGui.QColor('green'))
        painter.setPen(pen)
        for x in range(40):
            painter.drawPolyline(QtGui.QPolygon([
                QPoint(0+x*20, 500),
                QPoint(10+x*20, 490),
                QPoint(15+x*20, 480),
                QPoint(20+x*20, 465),
                QPoint(25+x*20, 440),
                QPoint(30+x*20, 405),
                QPoint(35+x*20, 380),
            ]))

        painter.end()
        self.label.setPixmap(canvas)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
