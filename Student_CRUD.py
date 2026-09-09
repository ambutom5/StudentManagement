import  mysql.connector

class Connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Anu@mbu5",
                database="luminar"
            )
            return self.connection
        except Exception as e:
            return None

class Student(Connect):
    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into studentt (id,name,age,place) values (%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Student Added!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from studentt"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            for row in record:
                print(row)
        except Exception as e:
            print(e)

    def get_id(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from studentt where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record

        except Exception as e:
            return None

    def retrieve(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                query = "delete from studentt where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Student Deleted!")
        except Exception as e:
            print(e)

    def put(self,id = None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update studentt set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Student Updated")
        except Exception as e:
            print(e)



student_instance = Student()
# student_instance.post(id = 6,name = "Mannu",age = 30,place = "Tirur")
# student_instance.get()
# student_instance.get_id(id = 5)
# student_instance.retrieve(id = 3)
# student_instance.delete(id = 6)
student_instance.put(id = 5,name = "Mannu",age = 30,place = "Tirur")








# import mysql.connector
# import datetime
# class Dbconnect:
#     def get_connect(self):
#         try:
#             self.connection=mysql.connector.connect(
#                 host="localhost",
#                 user="root",
#                 password="Anjana@123",
#                 database="company_db"
#             )
#             return self.connection
#         except Exception as e:
#             return None
#
# class EmployeeManager(Dbconnect):
#     def get_object(self,id=None):
#         try:
#             self.connect=super().get_connect()
#             self.cursor=self.connect.cursor()
#             query = "select * from employee where id=%s"
#             values = (id,)
#             self.cursor.execute(query, values)
#             records = self.cursor.fetchone()
#             return records
#         except Exception as e:
#             return None
#
#
#     def get(self):
#         try:
#             self.connect=super().get_connect()
#             self.cursor=self.connect.cursor()
#             query="select * from employee"
#             self.cursor.execute(query)
#             records=self.cursor.fetchall()
#             print(records)
#         except Exception as e:
#             print(e)
#
#
#     def post(self,id=None,**kwargs):
#         try:
#             self.connect = super().get_connect()
#             self.cursor = self.connect.cursor()
#             query="insert into employee (name,place,mobile,email,department,salary,joining_date) values(%s, %s, %s, %s, %s, %s, %s)"
#             values=[v for v in kwargs.values()]
#             self.cursor.execute(query,values)
#             self.connect.commit()
#             print("Employee Added Successfully")
#
#         except Exception as e:
#             print(e)
#
#     def retrieve(self,id=None):
#         try:
#             records=self.get_object(id=id)
#             if records==None:
#                 print("Employee not found")
#             else:
#                 print(records)
#         except Exception as e:
#             print(e)
#
#     def delete(self,id=None):
#         try:
#             records = self.get_object(id=id)
#             if records == None:
#                 print("Employee not found")
#             else:
#                 query="delete from employee where id=%s"
#                 values=(id,)
#                 self.cursor.execute(query,values)
#                 self.connect.commit()
#                 print("Employee deleted successfully")
#         except Exception as e:
#             print(e)
#
#     def put(self,id=None,**kwargs):
#         try:
#             records = self.get_object(id=id)
#             if records == None:
#                 print("Employee not found...!")
#             else:
#                 placeholder = ""
#                 for k in kwargs.keys():
#                     placeholder += k + "=%s,"
#                 placeholder = placeholder.rstrip(",")
#                 query = f"update employee set {placeholder} where id=%s"
#                 values = [v for v in kwargs.values()]
#                 values.append(id)
#                 self.cursor.execute(query, values)
#                 self.connect.commit()
#                 print("Employee updated successfully")
#
#         except Exception as e:
#             print(e)
#
#
# connection_instance = Dbconnect()
# print(connection_instance.get_connect())
#
# employee_instance = EmployeeManager()
#
# #employee_instance.post(name="Anjana",place="kochi",mobile="9876543211",email="anjana@gmail.com",department="IT",salary=30000,joining_date=datetime.date.today())
# #employee_instance.post(name="Arun",place="kottyam",mobile="9876643210",email="arun@gmail.com",department="IT",salary=20000,joining_date=datetime.date.today())
# #employee_instance.post(name="Arjun",place="kollam",mobile="1234567890",email="arjun@gmail.com",department="IT",salary=25000,joining_date=datetime.date.today())
# #employee_instance.get()
# #employee_instance.retrieve(id=1)
# # emp_instance.get_object(id=1)
# employee_instance.delete(id=3)