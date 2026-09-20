import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sonipy")
        self.resize(720,480)
        # self.setWindowOpacity(0.5)



app = QApplication(sys.argv)

window = MainWindow()
window.show()

def AppWindow():
    app.exec()