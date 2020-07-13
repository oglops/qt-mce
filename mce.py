from PySide2 import QtWidgets, QtCore

from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl

import sys
import os

class Window(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        layout = QtWidgets.QVBoxLayout()
        # button = QtWidgets.QPushButton('yeah')
        view = QWebEngineView()
        layout.addWidget(view)
        self.setLayout(layout)
        self.resize(800,600)

        url = 'file://'+ os.path.join(os.path.dirname(__file__), 'index.html')
        view.load(QUrl(url))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()