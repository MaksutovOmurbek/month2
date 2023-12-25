# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info_user(self):
#         print(f"Привет меня зовут {self.name} мне {self.age} лет")
    
# person = Person("geeks", 2)
# person.info_user()

# class Father:
#     def car(self):
#         print("У меня есть машина")


# # father = Father()
# # father.car()



# class Son(Father):
#     pass


# son = Son()
# son.car()


# class Father:
#     def info_father(self):
#         print("я отец")
# class Mum:
#      def info_mum(self):
#           print("Я Мама")


# class Son(Father):
#      def info_son(self):
#        print("Я сын")

# son = Son()
# son.info_father()
# son.info_son()
# son.info_mum()




# class Phone:
#     def call(self):
#         ("Я звоню маме")

# class Camera:
#     def take_photo(self):
#         print("Я фоткаю отца")

# class Smartphone(Phone,Camera):
#     def alll(self):
#         print("Я Фоткаю и так же звоню")
 
# smartphone = Smartphone()
# smartphone.call()
# smartphone.take_photo()
# smartphone.alll()

# class Animals:
#     def __init__(self, name):
#         self.name = name


# class Dog(Animals):
#     def sound(self):
#         return "гаф гаф гаф"
    

# dog = Dog("бульдог")
# print(f"{dog.name}:{dog.sound()}")


class User:
    def init(self, name, lastname, age, phone, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.phone = phone
        self.email = email
    def info(self):
        print(f"""Name: {self.name}
lastname: {self.lastname}
age: {self.age}
number: {self.phone}
email: {self.email}""")

user = User("Nur", "Nurov", 15, "+994445566", "nur@gmail.com")
user.info() 


# class Auto:
#     def __init__(self, mark, year) :
#         self._mark = mark
#         self._year = year


#     def info(self):
#         print(self._mark)

    
# auto = Auto("Lexus", 2023)
# auto.info()
# print(auto._year)
        
    

