import mysql.connector
from mysql.connector import Error


class Conector:
    def __init__(self):
        self.columnas = []
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='TFI',
                                                 user='root',
                                                 password='Mateo141020')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def select(self, query):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='TFI',
                                                 user='root',
                                                 password='Mateo141020')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                self.columnas = cursor.column_names
                record = cursor.fetchall()
                return record
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def call_stored_procedure(self, proceadure_name):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='TFI',
                                                 user='root',
                                                 password='Mateo141020')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.callproc(proceadure_name)
                self.columnas = cursor.column_names
                record = cursor.fetchall()
                return record
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def call_view(self, view_name):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='TFI',
                                                 user='root',
                                                 password='Mateo141020')
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM "+view_name)
                self.columnas = cursor.column_names
                record = cursor.fetchall()
                return record
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

