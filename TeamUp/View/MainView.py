# This Python file uses the following encoding: utf-8

from Control import MainControl

class MainView:

    def __init__(self):
        H=MainControl.MainControl()
        f=H.update("age",80,("idStudent",),(1,),0,"Student")
