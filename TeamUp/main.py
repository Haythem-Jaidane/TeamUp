# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication ,QMainWindow
from View import MainView
from Controller import MainControl

from PySide6.QtUiTools import QUiLoader
from PySide6 import QtGui

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        main=loader.load("UIdesgin/MainPage.ui", self)

        self.show()

if __name__ == "__main__":
    M=MainControl.MainControl()
    loader = QUiLoader()
    app = QApplication(sys.argv)
    window = loader.load("UIdesgin/MainPage.ui", None)
    window.logo.setPixmap(QtGui.QPixmap("Resources/Images/black_Logo_342868e838_129748d4cd.svg"))
    window.pen.setPixmap(QtGui.QPixmap("Resources/Images/pen.png"))
    window.Task.setPixmap(QtGui.QPixmap("Resources/Images/task-42.svg"))
    window.xp_icon.setPixmap(QtGui.QPixmap("Resources/Images/xpLogo.png"))
    window.profil_icon.setPixmap(QtGui.QPixmap("Resources/Images/profile-12.svg"))
    window.personality.setPixmap(QtGui.QPixmap("Resources/Images/noun-personality-4159972.svg"))
    H=M.read("Student")
    print(H[0][4])
    window.XP.setText(str(window.XP.text())+" : "+str(H[0][4]))
    window.Name.setText(H[0][1])
    window.Personality.setText(H[0][2])
    window.label_22.setText(H[0][5])
    A=M.read("project")
    window.show()
    sys.exit(app.exec())



