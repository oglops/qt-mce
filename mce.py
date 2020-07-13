#!/usr/bin/env python3
from PySide2 import QtWidgets, QtCore

from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl

import sys
import os
import pathlib


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        view = QWebEngineView()
        layout.addWidget(view)
        self.setLayout(layout)
        self.resize(900, 600)

        url = 'file://' + os.path.join(
            pathlib.Path(__file__).parent.absolute(), 'index.html'
        )
        print(url)
        view.load(QUrl(url))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
