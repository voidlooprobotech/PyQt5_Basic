import sys

from PyQt5.QtWidgets import  QApplication, QMainWindow, QMenuBar, QStatusBar, QAction

class TextPad(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        editmenu = menubar.addMenu('Edit')
        fontmenu = menubar.addMenu('Font')
        viewmenu = menubar.addMenu('Veiw')

        self.statusbar =  self.statusBar()
        self.statusbar.showMessage('Status Show')

        viewaction = QAction('View StatusBar', self, checkable=True)
        viewaction.setStatusTip('View StatusBar')
        viewaction.setChecked(True)
        viewmenu.triggered.connect(self.showhide)

        viewmenu.addAction(viewaction)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('MenuBar')
        self.show()

    def showhide(selfself, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

def main ():
    app = QApplication(sys.argv)
    textpad = TextPad()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()