import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QRect, QTimer
from PyQt5 import QtCore
from click import ClickHandler

GHOST_IDLE = 'assets/idle.gif'

def main():
    app = QApplication(sys.argv)

    # creates the widget base (UI object)
    w = QWidget()
    w.resize(250, 200)
    w.move(300, 300)

    # load in the default ghost and set its sizing etc
    idle_gif = QMovie(GHOST_IDLE)
    idle_gif.setScaledSize(QtCore.QSize(100, 100))

    label = QLabel(w)
    label.setGeometry(QRect(25, 25, 200, 200))
    label.setMovie(idle_gif)
    label.resize(100, 100)
    idle_gif.start()

    # makes the ghost always on top window
    w.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                     QtCore.Qt.FramelessWindowHint)
    w.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    w.show()

    # replace these attributes of w with the defined functions from ClickHandler
    click_handler = ClickHandler(w)
    w.mousePressEvent = click_handler.start_drag
    w.mouseMoveEvent = click_handler.drag_pet
    w.mouseReleaseEvent = click_handler.end_drag

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
