# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication

from Control import MainControl


if __name__ == "__main__":
    """base = DataBase.DataBase()
    f = base.connectMySQL()"""
    H=MainControl.MainControl()
    f=H.update("age",20,("idStudent",),(1,),0,"Student")
    app = QApplication([])
    # ...

    sys.exit(app.exec_())



