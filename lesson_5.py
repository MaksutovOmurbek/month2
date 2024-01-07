# import sqlite3

# connect = sqlite3.connect('users.db')
# cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS nurbolot(
#     id INTEGER PRIMARY KEY,
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     age  INTEGER           
# )''')



# # while True:
# #     first_name = input("введите имя: ")
# #     last_name = input("Введите фамилия: ")
# #     age = input("Введите возраст: ")

#     # cursor.execute(f'''INSERT INTO nurbolot(first_name, last_name, age) VALUES("{first_name}", "{last_name}", {age})''')
#     # connect.commit()
#     # connect.close()


# cursor.execute('''SELECT * FROM nurbolot''')
# data = cursor.fetchall()


# for result in data:
#     print(f"id: {result[0]}/n Имя: {result[1]}  Фамилия: {result[2]}  Возраст: {result[3]}/n")
# print("===============================================================================================")



