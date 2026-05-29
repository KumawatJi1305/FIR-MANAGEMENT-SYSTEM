import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="080512",
        database="fir___system"
    )
    return connection
