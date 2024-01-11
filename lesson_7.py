import sqlite3

connect = sqlite3.connect("bank.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
               id INTEGER PRIMARY KEY,
               name VARCHAR(255),
               surname VARCHAR(255),
               age INTEGER,
               bio TEXT,
               balance  INTEGER,
               wallet_id VARCHAR(16),
               email VARCHAR(255)
               )""")

class Bank:
    def __init__(self):
        self.name  = None
        self.surname  = None
        self.age  = None
        self.bio  = None
        self.balance  = 0
        self.wallet_id  = None
        self.email  = None
        
    def register(self, name,surname,age,email,bio):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.bio = bio
        cursor.execute(f""" INSERT INTO clients (name,surname,age,balance,wallet_id,email,bio) VALUES('{self.name}','{self.surname}',{self.age}, 0 ,'34423432','{self.email}','{self.bio}') """)
        connect.commit()

    def deposit(self, amount):
     cursor.execute(f"UPDATE clients SET balance = balance + {amount} WHERE email = '{self.email}' ")   
     connect.commit()     
     self.balance += amount
     print (f"\nУважаемый {self.name} {self.surname}. Поздравляем вы успешно выполнили баланс, на сумму: {self.balance} !!!\n ")
    print("===============================================================================================")
    
    def credit(self, subt):
        cursor.execute(f"UPDATE clients SET balance = balance - {subt}") 
        connect.commit()
        self.balance = subt
        print (f"\nУважаемый {self.name} {self.surname}. Поздравляем вы успешно забрали деньги, на сумму: {self.balance} и осталось {self.balance} !!!\n")
        print("===============================================================================================")
        
    def main(self):
        while True:
            commands = input("1 - регистрация, 2 - информация, 3 - пополнить, 6 - забрать, 4 - вывести, 5 - выйти, 6 - забрать: ")
            if commands =="1":
                print("===============================================================================================")
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                age = int(input("Введите возраст: "))
                bio = input("Введите биографию: ")
                email = input("Введите почту(example@gmail.com): ")
                print("===============================================================================================")
                if "@gmail.com" in email:
                    if age >=17:
                        self.register(name,surname,age,email,bio)
                        print(f"\nУважаемый {name} {surname}. Поздравляем вы успешно прошли регистрацию!!!\n")
                        print("===============================================================================================")

                    else:
                        continue
                else:
                    continue
            elif commands == "3":
                num = int(input("Введите сумму: "))
                self.deposit(num)

            elif commands == "6":
                doc = int(input("Сколько возмете: "))
                self.credit(doc)
            
            elif commands =="2":
                    print(''' Наш Банк Optima работаем 2014 года, 
                          находимся Мырзалы Аматов 1Б если проблемы optima@gmail.com,
                          если хотите связаться 01212121
                                                01212121
                                                01212121''')
                    
            elif commands == "5":
                print("ошибка!!!!!")

            else:
                print("Такой команды нет")
                

bank = Bank()
bank.main()





     

