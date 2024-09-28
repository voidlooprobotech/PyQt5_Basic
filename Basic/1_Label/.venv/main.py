import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def main():
    app = QApplication(sys.argv)
    widget = QWidget()

    text = QLabel(widget)
    text.setText("PyQt App Test")
    font = QFont()
    font.setPointSize(24)
    font.family()
    text.setFont(font)
    text.move(120, 80)


    widget.setGeometry(100, 100, 500, 500)
    widget.setWindowTitle("Label Demo Application")
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()