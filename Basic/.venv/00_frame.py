import sys

from PyQt5.QtWidgets import QApplication, QWidget

def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(500,550)
    widget.setWindowTitle("First PyQt Application")
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()