#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QListWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(400, 390, 230, 290)
        self.lst = QListWidget()
        self.lst.itemDoubleClicked.connect(self.replaceitem)
        self.inp = QLineEdit()
        self.inp.returnPressed.connect(self.replacetxt)
        self.create()

    def create(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.inp)
        vbox.addWidget(self.lst)
        self.setLayout(vbox)

    def replacetxt(self):
        self.lst.addItem(self.inp.text())
        self.inp.clear()

    def replaceitem(self):
        listItems = self.lst.selectedItems()
        if not listItems:
            return None
        for item in listItems:
            self.inp.setText(item.text())


def main():
    app = QApplication(sys.argv)
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
