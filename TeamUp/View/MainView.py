# This Python file uses the following encoding: utf-8

from Controller import MainControl
from PyQt6.QtWidgets import QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PyQt6 import uic
import os
from pathlib import Path

class MainView(QWidget):

    def __init__(self):
        super(MainView, self).__init__()
        self.load_ui(self)

    def load_ui(self,window):
        loader = QUiLoader()
        path = "./UIdesgin/MainPage.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

