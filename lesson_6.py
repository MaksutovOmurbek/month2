# class Dad:
#     def dad_info(self):
#         return " Это от деда"
# class Father(Dad):
#      def father_info(self):
#         return " это от отца"
# class Son(Father):
#      def son_info(self):
#         return " это от сына"

# # dad = Dad()
# # print(dad.dad_info())
     
# # father = Father()
# # print(father.father_info())
# # print(father.dad_info())
     

# son = Son()
# print(son.son_info())
# print(son.father_info())
# print(son.dad_info())


# class Dad:
#     def dad_info(self):
#         return "Это от деда"
# class Father(Dad):
#     def father_info(self):
#         return "Это от отца"
# class Son(Father):
#     def son_info(self):
#         return "Это от сына!"
    
# dad = Dad()
# print(dad.dad_info())
    
# father = Father()
# print(father.father_info())
# print(father.dad_info())
    
# son = Son()
# print(son.son_info())
# print(son.dad_info())
# print(son.father_info())


# import sqlite3
# import   random
# class Game:
#     def game(self):
#  connect  = sqlite3.connect("users_random.db")
#  cursor = connect.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS clients(
#             name VARCHAR(255),
#             surname VARCHAR(255),
#             age INTEGER,
#             email VARCHAR(255),
#             password VARCHAR(255)
# )''')
#         n = 0 
#         limit = 5
#         while True:
#             randon = random.randint(1,5)
#             user = int(input("Введите число: "))
#             limit-=1

#             if limit != 0:
#                 if n !=4:
#                     if user ==randon:
#                         n +=1
#                         print(f"Вы угадали, Бот выбрал: {randon}. Выигрыш: {n}. Количество попыток: {limit}")
#                     else:
#                         print(f"Вы не угадали, Бот выбрал: {randon}. Выигрыш: {n}. Количество попыток: {limit}")

#                 else:
#                     print(f"Вы выиграли, у вас 5 баллов!!! Выигрыш: {n}. Количество попыток: {limit}")
#                     break
#             else:
#                 print(f"Вы проиграли, у вас закончились попытки!!! Выигрыш: {n}. Количество попыток: {limit}")
#                 break


#     def register(self,name,surname,age,email,password,confirm_password):
#         if password ==confirm_password:
#             cursor.execute(f'''INSERT INTO clients(name,surname,age,email,password) VALUES('{name}','{surname}',{age},'{email}','{password}')''')
#             connect.commit()
#             print("")
#             print(f"Уважаемый {name} {surname},Вы успешно прошли регистрацию")
#             print("")
#             self.game()
#         else:
#             print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароли не совпадают !!")
                

#     def main(self):
#         name = input("Введиие имя: ")
#         surname = input("Введите фамилию: ")
#         age = int(input("Введите возраст: "))
#         email = input("Введите почту: ")
#         password = input("Введите пароль: ")
#         confirm_password = input("Потвердите пароль: ")
#         if age >=18:
#             if len(password) >=8:
#                 if "123" not in password:
#                     self.register(name,surname,age,email,password,confirm_password)
#                 else:
#                     print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароль простой!!")
#             else:
#                 print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Пароль короткий!!")
#         else:
#             print(f"Уважаемый {name} {surname}, вы не прошли регистрацию. Вам нет 18лет!!")

# game_user = Game()
# game_user.main()





