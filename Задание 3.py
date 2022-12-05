#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QTextEdit,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QApplication.instance().focusChanged.connect(self.on_focusChanged)
        self.setWindowTitle("MyApp")
        self.setGeometry(370, 390, 300, 390)
        self.inp1 = QLineEdit()
        self.inp2 = QLineEdit()
        self.inp2.returnPressed.connect(self.edit_size)
        self.txtbox = QTextEdit()
        self.btn = QPushButton("Изменить")
        self.btn.clicked.connect(self.edit_size)
        self.widget()

    def widget(self):
        inpbox = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        inpbox.addWidget(self.inp1)
        inpbox.addWidget(self.inp2)
        hbox.addLayout(inpbox)
        hbox.addWidget(self.btn)
        vbox.addLayout(hbox)
        vbox.addWidget(self.txtbox)
        self.setLayout(vbox)
        self.w = 0
        self.h = 0

    def edit_size(self):
        self.w = int(self.inp1.text())
        self.h = int(self.inp2.text())
        self.txtbox.resize(self.w, self.h)

    def on_focusChanged(self, old, now):
        if self.txtbox == now:
            self.txtbox.setStyleSheet(f"background-color: white;")
            self.txtbox.resize(self.w, self.h)
        elif self.txtbox == old:
            self.txtbox.setStyleSheet(f"background-color: lightgrey;")
            self.txtbox.resize(self.w, self.h)


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
