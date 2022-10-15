# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication

from View import MainView


if __name__ == "__main__":

    MainView.MainView()
    app = QApplication([])
    # ...

    sys.exit(app.exec_())



