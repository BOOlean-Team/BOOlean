import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QRect

from PyQt5 import QtCore


def main():
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 200)
    w.move(300, 300)

    gif = QMovie('assets/idle.gif')
    gif.setScaledSize(QtCore.QSize(100, 100))

    label = QLabel(w)
    label.setGeometry(QRect(25, 25, 200, 200))
    label.setMovie(gif)
    label.resize(100, 100)
    gif.start()

    w.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                     QtCore.Qt.FramelessWindowHint)
    w.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
