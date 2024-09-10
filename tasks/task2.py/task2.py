import sqlite3

def create_students_table():
    try:
      
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()

       
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade REAL
            )
        ''')

        print("Table 'students' created successfully or already exists.")

        \
        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

create_students_table()


import sqlite3

def insert_students_data():
    try:
        # Подключение к базе данных
        connection = sqlite3.connect("school.db")
        cursor = connection.cursor()

        # Данные для вставки
        students_data = [
            (1, 'Alice', 20, 3.8),
            (2, 'Bob', 21, 3.5),
            (3, 'Charlie', 22, 3.9)
        ]

        # Вставка данных в таблицу
        cursor.executemany('''
            INSERT INTO students (id, name, age, grade)
            VALUES (?, ?, ?, ?)
        ''', students_data)

        # Сообщение об успешной вставке данных
        print("Data inserted successfully into 'students' table.")

        # Сохранение изменений и закрытие соединения
        connection.commit()
        connection.close()

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Вызов функции для вставки данных
insert_students_data()
