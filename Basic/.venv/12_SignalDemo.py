import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication

class SignalDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("Event and Signal Application Demo")
        self.show()
def main():
    app = QApplication(sys.argv)
    widget = SignalDemo()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()



