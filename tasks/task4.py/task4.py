import sqlite3

def query_students_data():
    try:
      
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()

        print("ID | Name    | Age | Grade")
        print("--------------------------")
        for row in rows:
            print(f"{row[0]:<2} | {row[1]:<7} | {row[2]:<3} | {row[3]:<4.1f}")

        connection.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

query_students_data()
