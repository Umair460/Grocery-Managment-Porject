import mysql.connector
from mysql.connector import Error

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(user='root', password='Umair@720',
                                            host='127.0.0.1',
                                            database='gs')
        except Error as e:
            print(f"Error: {e}")
            __cnx = None
    return __cnx
