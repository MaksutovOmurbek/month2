# class Student:
#     def __init__(self, name, well, ticket, surname):
#         self.name = name
#         self.surname = surname
#         self.well = well
#         self.ticket = ticket

#     def info(self):
#         print(f'''Name: {self.name}
# Фамилия: {self.surname}
# Cписок курса: {self.well}
# Студентский билет: {self.ticket}''')


# student = Student("Omurbek", "geeks", "13", "Maksutov")
# student.info()


# import math


# class Library:
#  def borrow_book(self, title):
#         for book in self.books:
#             if book["title"] == title and book["status"] == "доступна":
#                 book["status"] = "выдана"
#                 print(f"Книга '{title}' успешно выдана.")
#                 return True
#             elif book["title"] == title and book["status"] == "выдана":
#                 print(f"Книга '{title}' уже выдана.")
#                 return False
#         print(f"Книга '{title}' не найдена в библиотеке или уже выдана.")
#         return False

# def return_book(self, title):
#         for book in self.books:
#             if book["title"] == title and book["status"] == "выдана":
#                 book["status"] = "доступна"
#                 print(f"Книга '{title}' успешно возвращена.")
#                 return True
#             elif book["title"] == title and book["status"] == "доступна":
#                 print(f"Книга '{title}' уже доступна в библиотеке.")
#                 return False
#         print(f"Книга '{title}' не найдена в библиотеке или еще не выдана.")
#         return False

# library = Library()

# library.add_book("Мастер и Маргарита", "Михаил Булгаков")
# library.add_book("1984", "Джордж Оруэлл")

# library.borrow_book("Мастер и Маргарита")
# library.borrow_book("1984")

# library.return_book("Мастер и Маргарита")
# library.return_book("1984")

# library.remove_book("1984")











