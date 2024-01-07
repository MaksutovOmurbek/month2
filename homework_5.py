import sqlite3

connect = sqlite3.connect("car.db")
cursor = connect.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS car(
    id INTEGER PRIMARY KEY,
    model VARCHAR(255),
    marka VARCHAR(255),
    year INTEGER,
    description VARCHAR(255),
    status VARCHAR(255))''')


def to_create():
    marka = input("Ввете марку машины: ")
    model  = input("Введите модель машины : ")
    year = int(input("Введите год машины: "))
    description = input("Введите описание машины: ")
    status = input("Введите статус машины: ")


    
    cursor.execute(f'''INSERT INTO car(model, marka, year, description, status) VALUES( "{model}","{marka}", {year}, "{description}", "{status}")''')
    connect.commit()
    connect.close()

