
import mysql.connector
from mysql.connector import Error
from config import config

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("The connection is closed")
