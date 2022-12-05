#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import QWidget, QApplication
from PySide2.QtCore import QPoint, QPropertyAnimation


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color: green; border-radius: 30%;")
        self.child.resize(60, 60)
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setDuration(1500)

    def mousePressEvent(self, event):
        self.anim.setEndValue(QPoint(event.x() - 25, event.y() - 25))
        self.anim.start()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
