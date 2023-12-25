# import random

# class SlotMachine:
#     def __init__(self, name):
#         self.name = name
#         self.user_balance = 100
#         self.game_balance = 0

#     def info(self):
#         print(f"Имя игрока: {self.name}")
#         print(f"Пользовательский баланс: {self.user_balance}$")
#         print(f"Игровой баланс: {self.game_balance}$")

#     def top_up_balance(self, amount):
#         if amount > 100:
#             print("Вы можете пополнить до 100$")
#         else:
#             self.balance_up(amount)

#     def balance_up(self, amount):
#         self.user_balance -= amount
#         self.game_balance += amount

#     def game(self):
#         number_to_guess = random.randint(1, 10)
#         attempts = 5

#         while attempts > 0:
#             guess = int(input("Угадайте число от 1 до 10: "))
#             if guess == number_to_guess:
#                 print("Вы выиграли!")
#                 self.game_balance += 50
#                 return
#             else:
#                 self.user_balance -= 10
#                 print("Вы не угадали")
#                 attempts -= 1
        
#         print("Вы проиграли!")

#     def conclusion_money(self, amount):
#         if amount < 50:
#             print("Вывести можно от 50$")
#         else:
#             self.user_balance += amount
#             self.game_balance -= amount
#             print("Деньги успешно выведены")

#     def main(self):
#         while True:
#             command = int(input("Введите команду (1, 2, 3, 4): "))

#             if command == 1:
#                 self.info()
#             elif command == 2:
#                 amount = int(input("Введите сумму для пополнения: "))
#                 self.top_up_balance(amount)
#             elif command == 3:
#                 self.game()
#             elif command == 4:
#                 amount = int(input("Введите сумму для вывода: "))
#                 self.conclusion_money(amount)
#             else:
#                 print("Неверная команда")


# slot_machine = SlotMachine("Игрок")
# slot_machine.main()








        

