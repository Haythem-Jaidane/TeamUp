# This Python file uses the following encoding: utf-8

from Model import DataBase

class MainControl:
    def __init__(self):
        self.base = DataBase.DataBase().connectMySQL()

    def read(self,table_name):
        mycursor = self.base.cursor()
        mycursor.execute("SELECT * FROM "+table_name)
        return mycursor.fetchall()

    def create(self,colum,values,table_name):
        create_qury = "Insert into "+str(table_name)+" ( "
        for i in range(len(colum)):
            create_qury+=str(colum[i])
            if (i != len(colum)-1 ):
                create_qury+=","
            else:
                create_qury+=") "
        create_qury+="VALUES ("
        for i in range(len(values)):
            if(isinstance(values[i],str)):
                create_qury+="\""+str(values[i])+"\""
            else:
                create_qury+=str(values[i])
            if (i != len(values)-1 ):
                create_qury+=","
            else:
                create_qury+=") "
        mycursor = self.base.cursor()
        mycursor.execute(create_qury)
        self.base.commit()

    def update(self,change_colum,new_value,colum_condition,value_condition,operation,table_name):
        update_qury = "UPDATE "+table_name+" SET "+str(change_colum)+" = "
        if(isinstance(new_value,str)):
            update_qury+="\""+str(new_value)+"\""
        else:
            update_qury+=str(new_value)
        update_qury += " WHERE "
        for i in range(len(colum_condition)):
            update_qury += str(colum_condition[i])+" = "
            #print(value_condition)
            if(isinstance(value_condition[i],str)):
                update_qury+="\""+str(value_condition[i])+"\""
            else:
                update_qury+=str(value_condition[i])
            if(operation==1):
                update_qury+=" AND "
            elif(operation==2):
                update_qury+=" OR "
            else:
                break
        mycursor = self.base.cursor()
        mycursor.execute(update_qury)
        self.base.commit()


    def delete(self,table_name,colum,value,operation):
        delate_qury = "DELETE FROM "+table_name+" WHERE "
        for i in range(len(colum)):
            delate_qury+=str(colum[i])+" = "
            print(value[i])
            if(isinstance(value[i],str)):
                delate_qury+="\""+str(value[i])+"\""
            else:
                delate_qury+=str(value[i])
            if(operation==1):
                delate_qury+=" AND "
            elif(operation==2):
                delate_qury+=" OR "
            else:
                break
        mycursor = self.base.cursor()
        mycursor.execute(delate_qury)
        self.base.commit()
