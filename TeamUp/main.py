# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication ,QMainWindow
from View import MainView
from Controller import MainControl

from PySide6.QtUiTools import QUiLoader
from PySide6 import QtGui


if __name__ == "__main__":
    viewOject=MainView.MainView()
    app = QApplication(sys.argv)
    viewOject.window=viewOject.renderPage("UIdesgin/logIn.ui")
    viewOject.window.submit_button.clicked.connect(viewOject.submit_button)


    """M=MainControl.MainControl()
    loader = QUiLoader()
    app = QApplication(sys.argv)

    H=M.read("Student")
    print(H[0][4])
    window.XP.setText(str(window.XP.text())+" : "+str(H[0][4]))
    window.Name.setText(H[0][1])
    window.Personality.setText(H[0][2])
    window.label_22.setText(H[0][5])
    A=M.read("project")"""
    viewOject.window.show()
    sys.exit(app.exec())



