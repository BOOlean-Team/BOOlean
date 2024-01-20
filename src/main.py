import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QRect, QTimer
from PyQt5 import QtCore
from click import ClickHandler

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

    click_handler = ClickHandler(w)
    w.mousePressEvent = click_handler.start_drag
    w.mouseMoveEvent = click_handler.drag_pet
    w.mouseReleaseEvent = click_handler.end_drag

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
