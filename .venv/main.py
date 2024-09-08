import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Void Loop Robotech")
        self.setGeometry(700, 300, 500, 500)
        self.setWindowIcon( QIcon("logo1.png"))
        label = QLabel("void loop robotech", self)
        label.setFont(QFont("Arial", 18))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #0707f2;"
                            "background-color: #efff08;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        #label.setAlignment(Qt.AlignTop)  #verically TOP
        #label.setAlignment(Qt.AlignBottom)  #verically BOttom
        #label.setAlignment(Qt.AlignVCenter)  # verically Center
        #label.setAlignment(Qt.AlignRight)  # Horizontlly Right
        #label.setAlignment(Qt.AlignVCenter)  # Horizontlly Center
        #label.setAlignment(Qt.AlignLeft)  # Horizontlly Left

        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)  #Center & top
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)  # Center & bottom
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # Center & center

        label.setAlignment(Qt.AlignCenter)  # Center & center




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())




if __name__ == "__main__":
    main()

