import  sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication

class NameInput(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.btn = QPushButton('Click Me', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.name = QLineEdit(self)
        self.name.move(130, 20)

        self.setGeometry(400, 300, 400, 300)
        self.setWindowTitle('Dialog Box')
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Name Dialog Box', 'Enter Your Label: ')
        if ok:
            self.name.setText(str(text))
def main():
    app = QApplication(sys.argv)
    widget = NameInput()
    sys.exit(app.exec_())

if __name__  == '__main__':
    main()




