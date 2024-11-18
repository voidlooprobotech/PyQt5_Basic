import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class ToolBarDemo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        exitaction = QAction(QIcon('exit.png'), 'Exit', self)
        exitaction.setShortcut('Ctrl+E')
        exitaction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitaction)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Tool Bar Application Demo")
        self.show()

def main():
    app = QApplication(sys.argv)
    widget = ToolBarDemo()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
