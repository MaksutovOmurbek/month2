# import sqlite3

# connect = sqlite3.connect("car.db")
# cursor = connect.cursor()



# cursor.execute('''CREATE TABLE IF NOT EXISTS car(
#     model INTEGER PRIMARY KEY,
#     marka VARCHAR(255),
#     number VARCHAR(255),
#     year INTEGER  )''')


# while True:
#     number = input("Введите номер машины: ")
#     marka = input("Ввете марку машины: ")
#     model  = input("Введите модель машины : ")
#     year = input("Введите год машины: ")

    
#     cursor.execute(f'''INSERT INTO car(model, marka, number, year) VALUES("{number}", "{marka}", "{model}", "{year})''')
#     connect.commit()
#     connect.close()

    
#     cursor.execute('''SELECT * FROM car''')
#     data = cursor.fetchall()


#     for result in data:
#         print(f"number: {result[0]}/n model: {result[1]}/n  marka: {result[2]}/n  year: {result[3]}/n")
#         print("===============================================================================================")