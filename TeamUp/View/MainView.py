# This Python file uses the following encoding: utf-8

from Controller import MainControl
from PyQt6.QtWidgets import QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import os
from pathlib import Path
from PySide6 import QtGui,QtWidgets
from Controller import MainControl

class MainView(QMainWindow):

    def __init__(self):
        self.islogin = False
        self.loader = QUiLoader()
        self.window = ""

    def renderPage(self,path):
        return self.loader.load(path, None)

    def configMainProject(self,window):
        window.logo.setPixmap(QtGui.QPixmap("Resources/Images/logo_black.svg"))
        window.pen.setPixmap(QtGui.QPixmap("Resources/Images/pen.png"))
        window.Task.setPixmap(QtGui.QPixmap("Resources/Images/task-42.svg"))
        window.xp_icon.setPixmap(QtGui.QPixmap("Resources/Images/xpLogo.png"))
        window.profil_icon.setPixmap(QtGui.QPixmap("Resources/Images/profile-12.svg"))
        window.personality_icon.setPixmap(QtGui.QPixmap("Resources/Images/noun-personality-4159972.svg"))


    def submit_button(self):
        self.window.close()
        self.window=self.renderPage("UIdesgin/MainPage.ui")
        self.configMainProject(self.window)
        self.window.setWindowTitle("TeamUp")
        M=MainControl.MainControl()
        H=M.read("Student")
        self.window.XP.setText(f"{str(self.window.XP.text())} : {str(H[0][4])}")
        self.window.Name.setText(H[0][1])
        self.window.Personality.setText(H[0][2])
        self.window.label_22.setText(H[0][5])
        A=M.read("project")
        self.window.Join_Forum.clicked.connect(self.test_personality)
        self.window.show()

        return self.window

    def test_personality(self):
        self.window.close()
        self.window=self.renderPage("UIdesgin/PersonalityTest.ui")
        self.window.show()
