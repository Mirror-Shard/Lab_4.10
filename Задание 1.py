#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QAbstractItemView,
)


class MainWindow(QWidget):
    def __init__(self, food):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.setGeometry(400, 390, 450, 200)
        self.lst1 = QListWidget()
        self.lst1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst2 = QListWidget()
        self.lst2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst1.addItems(food)
        self.but1 = QPushButton(">>>")
        self.but2 = QPushButton("<<<")
        self.setting()

    def setting(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.lst1)
        hbox.addLayout(vbox)
        vbox.addStretch()
        vbox.addWidget(self.but1)
        vbox.addWidget(self.but2)
        vbox.addStretch()
        hbox.addWidget(self.lst2)
        self.setLayout(hbox)
        self.but1.clicked.connect(self.ToRight)
        self.but2.clicked.connect(self.ToLeft)

    def ToRight(self):
        for item in self.lst1.selectedItems():
            self.lst1.takeItem(self.lst1.row(item))
            self.lst2.addItem(item)

    def ToLeft(self):
        for item in self.lst2.selectedItems():
            self.lst2.takeItem(self.lst2.row(item))
            self.lst1.addItem(item)


def main():
    app = QApplication(sys.argv)
    food = (
        "apple",
        "bananas",
        "carrot",
        "bread",
        "butter",
        "meat",
        "potato",
    )
    application = MainWindow(food)
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
