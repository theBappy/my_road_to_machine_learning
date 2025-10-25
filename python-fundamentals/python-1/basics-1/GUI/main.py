import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 200, 500, 500)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     main()


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My Cool first GUI")
#         self.setGeometry(500, 200, 500, 500)
#         self.setWindowIcon(QIcon("icon.png"))

#         label = QLabel("Hello", self)
#         label.setFont(QFont("Jost", 30))
#         label.setGeometry(0, 0, 500, 100)
        # label.setStyleSheet("color: #292929;", "background-color:#6fdcf7;", "font-weight:bold;","font-style: italic;")

        # label.setAlignment(Qt.AlignTop) 
        # label.setAlignment(Qt.AlignBottom) 
        # label.setAlignment(Qt.AlignVCenter) 
        # label.setAlignment(Qt.AlignRight)
        # label.setAlignment(Qt.AlignHCenter) 
        # label.setAlignment(Qt.AlignLeft)

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)

        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # label.setAlignment(Qt.AlignCenter)

