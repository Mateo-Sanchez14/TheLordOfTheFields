import mysql.connector
from mysql.connector import Error


class Conector:
    def __init__(self):
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
                record = cursor.fetchall()
                return record
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
