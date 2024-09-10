import sqlite3

def insert_students_data():
    try:
   
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()

     
        students_data = [
            (1, 'Alice', 20, 3.8),
            (2, 'Bob', 21, 3.5),
            (3, 'Charlie', 22, 3.9)
        ]

        print("Data inserted successfully into 'students' table.")

       
        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

insert_students_data()
