import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS nurbolot(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age  INTEGER           
)''')

cursor.execute('''INSERT INTO nurbolot(first_name, last_name, age)  VALUES("Omurbek", "Maksutov", 18)''')
connect.commit()
connect.close()

