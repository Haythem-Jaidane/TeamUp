# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication
from PyQt6.QtWidgets import QWidget
from View import MainView

from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()

        # loading the ui file with uic module
        uic.loadUi("UIdesgin/MainPage.ui", self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = UI()
    window.setWindowTitle("TeamUp")
    window.show()
    sys.exit(app.exec_())



