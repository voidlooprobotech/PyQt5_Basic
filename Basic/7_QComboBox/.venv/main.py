import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel


class Price(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        price = QComboBox(self)

        price.addItem("0-100")
        price.addItem("100-200")
        price.addItem("200-300")
        price.addItem("300-400")
        price.addItem("400-500")
        price.addItem("500+")

        price.move(50, 50)

        self.label = QLabel(self)
        self.label.move(50, 20)
        price.activated[str].connect(self.onChanged)

        self.setGeometry(50, 50, 320, 300)
        self.setWindowTitle("ComboBox Application Demo")
        self.show()

    def onChanged(self, text):
        self.label.setText(text)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Price()
    sys.exit(app.exec_())






