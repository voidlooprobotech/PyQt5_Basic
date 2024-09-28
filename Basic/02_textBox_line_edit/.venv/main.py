import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton


def main():
    app = QApplication(sys.argv)
    widget = QWidget()

    label = QLabel(widget)
    label.move(20, 50)
    label.setText("Enter your name: ")

    name = QLineEdit(widget)
    name.move(125, 50)

    submit = QPushButton(widget)
    submit.move(135, 75 )
    submit.setText("Submit")

    widget.setGeometry(100, 100, 400, 400)
    widget.setWindowTitle("Label Demo Application")
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()