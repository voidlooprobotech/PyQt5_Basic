import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton

class App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.label = QLabel(self)
        self.label.move(20, 50)
        self.label.setText("Enter your name: ")

        self.name = QLineEdit(self)
        self.name.move(125, 50)

        submit = QPushButton(self)
        submit.move(135, 75 )
        submit.setText("Submit")
        submit.clicked.connect(self.showname)

    def showname(self):
        a = self.name.text()
        print(a)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = App()

    widget.setGeometry(100, 100, 400, 400)
    widget.setWindowTitle("Label Demo Application")
    widget.show()

    sys.exit(app.exec_())