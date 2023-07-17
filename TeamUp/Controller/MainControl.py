# This Python file uses the following encoding: utf-8

from Model import DataBase

class MainControl:
    def __init__(self):
        self.base = DataBase.DataBase().connectMySQL()

    def execute_to_db(self,qury):
        mycursor = self.base.cursor()
        mycursor.execute(qury)
        self.base.commit()

    def check_string_type(self,qury,value):
        if(isinstance(value,str)):
            qury+="\""+str(values[i])+"\""
        else:
            qury+=str(values[i])

    def check_and_or(self,operation):
        if (operation==1):
            delate_qury+=" AND "
        elif(operation==2):
            delate_qury+=" OR "

    def read(self,table_name):
        mycursor = self.base.cursor()
        mycursor.execute(f"SELECT * FROM {table_name}")
        return mycursor.fetchall()

    def create(self,colum,values,table_name):
        create_qury = f"Insert into {str(table_name)} ( "
        for i in range(len(colum)):
            create_qury+=str(colum[i])
            create_qury += "," if (i != len(colum)-1 ) else ") "
        create_qury+="VALUES ("
        for i in range(len(values)):
            check_string_type(create_qury,values[i])
            create_qury += "," if (i != len(values)-1 ) else ") "
        self.execute_to_db(create_qury)

    def update(self,change_colum,new_value,colum_condition,value_condition,operation,table_name):
        update_qury = f"UPDATE {table_name} SET {str(change_colum)} = "
        check_string_type(update_qury,new_value)
        update_qury += " WHERE "
        for i in range(len(colum_condition)):
            update_qury += f"{str(colum_condition[i])} = "
            check_string_type(update_qury,value_condition)
            self.check_and_or(operation)
        self.execute_to_db(update_qury)


    def delete(self,table_name,colum,value,operation):
        delate_qury = f"DELETE FROM {table_name} WHERE "
        for i in range(len(colum)):
            delate_qury += f"{str(colum[i])} = "
            check_string_type(update_qury,value[i])

        self.execute_to_db(delate_qury)
