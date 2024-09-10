import sqlite3

def connect_to_database(db_name):
    try:
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        print("Connection to the database was successful.")
        
        return connection, cursor
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None, None

db_name = "school.db"
connection, cursor = connect_to_database(db_name)

if connection:
    connection.close()
