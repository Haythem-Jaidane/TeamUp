# This Python file uses the following encoding: utf-8

import mysql.connector

class DataBase:

    def __init__(self , host = "localhost" ,user = "root" , password = ""):
        self.host = host
        self.user = user
        self.password = password

    def connectMySQL(self):
        try:
            mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            return mydb
        except:
            raise("check your database")
            return null

