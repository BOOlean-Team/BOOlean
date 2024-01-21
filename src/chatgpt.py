from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from services.chatgptAPI import get_response


class NewChatGPTWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 300)
        self.setStyleSheet(
            """
            border-image: url(assets/img/ghost_rect_box.png);
            padding: 20px 20px 80px 20px
            """)

        self.text_edit = TextEdit()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowStaysOnTopHint)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.text_edit)

        self.setLayout(self.layout)


class TextEdit(QTextEdit):
    DEFAULT_TEXT = 'Hi! How can I help you?'

    def __init__(self, *args, **kwargs):
        QTextEdit.__init__(self, *args, **kwargs)

        font = QFont('Helvetica', 14)
        font.setBold(True)

        self.setFont(font)
        self.setTextColor(QColor('Black'))
        # self.setFontWeight(QFont.bold)
        self.append(TextEdit.DEFAULT_TEXT + '\n')

        self.counter = 1
        self.prefix = ""
        self.callPrefix()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(
            self.onCustomContextMenuRequest)

    def onCustomContextMenuRequest(self, point):
        menu = self.createStandardContextMenu()
        for action in menu.actions():
            if "Delete" in action.text():
                action.triggered.disconnect()
                menu.removeAction(action)
            elif "Cut" in action.text():
                action.triggered.disconnect()
                menu.removeAction(action)
            elif "Paste" in action.text():
                action.triggered.disconnect()

        act = menu.exec_(point)
        if act:
            if "Paste" in act.text():
                self.customPaste()

    def customPaste(self):
        self.moveCursor(QTextCursor.End)
        self.insertPlainText(QApplication.clipboard().text())
        self.moveCursor(QTextCursor.End)

    def clearCurrentLine(self):
        cs = self.textCursor()
        cs.movePosition(QTextCursor.StartOfLine)
        cs.movePosition(QTextCursor.EndOfLine)
        cs.select(QTextCursor.LineUnderCursor)
        text = cs.removeSelectedText()

    def isPrefix(self, text):
        return self.prefix == text

    def getCurrentLine(self):
        cs = self.textCursor()
        cs.movePosition(QTextCursor.StartOfLine)
        cs.movePosition(QTextCursor.EndOfLine)
        cs.select(QTextCursor.LineUnderCursor)
        text = cs.selectedText()
        return text

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            command = self.getCurrentLine()[len(self.prefix):]
            self.execute(command)
            self.callPrefix()
            return
        elif event.key() == Qt.Key_Backspace:
            if self.prefix == self.getCurrentLine():
                return
        elif event.matches(QKeySequence.Delete):
            return
        if event.matches(QKeySequence.Paste):
            self.customPaste()
            return
        elif self.textCursor().hasSelection():
            t = self.toPlainText()
            self.textCursor().clearSelection()
            QTextEdit.keyPressEvent(self, event)
            self.setPlainText(t)
            self.moveCursor(QTextCursor.End)
            return
        QTextEdit.keyPressEvent(self, event)

    def callPrefix(self):
        self.prefix = ">>> "
        self.counter += 1
        self.append(self.prefix)

    def execute(self, command):
        response = get_response(command)
        self.append(response + '\n')
