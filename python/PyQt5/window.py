import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # Set ToolTip for main Window
        QToolTip.setFont(QFont('SansSerif', 10))

        # Button and ToolTip
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Quit', self)
        btn.clicked.connect((QCoreApplication.instance().quit))
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(0, 0)

        # Button to print to terminal
        btn = QPushButton('Say Hello', self)
        btn.clicked.connect(self.sayHello)
        btn.resize(btn.sizeHint())
        btn.move(100, 0)

        # Set size of the window
        self.setGeometry(300, 300, 300, 220)
        # Set Window Title
        self.setWindowTitle('Icon')
        # Set Window Icon
        self.setWindowIcon(QIcon('web.png'))

        # Call center method
        self.center()

        # Show the window
        self.show()

    def sayHello(self):
        print('Hello')

    def center(self):
        qr = self.frameGeometry()
        # Get size of monitor
        cp = QDesktopWidget().availableGeometry().center()
        # Move frame to the center
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
        "Are you sure to quit?", QMessageBox.Yes |
        QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
