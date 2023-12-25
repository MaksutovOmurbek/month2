class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


    def login(self):
        print(f"{self.name} is logging in...")

user = User("Max", "Max@gmail.com", "123")
user.login()

class Student(User):
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id
        self.courses_enrolled = []

    def enroll_in_course(self, course):
        self.courses_enrolled.append(course)
        print(f"{self.name} enrolled in {course}")

student1 = Student("Nurbolot", "Nurbolot@gmail.com", "02123", "S001")
student1.login()
student1.enroll_in_course("Backend")

class Teacher(User):
    def __init__(self, name, email, password, teacher_id):
        User.__init__(self, name, email, password)
        self.teacher_id = teacher_id
        self.courses_teaching = []


 
    

teacher = Teacher("Askat", "Askat@gmail.com", "01123", 1)
teacher.login()


class Admin(User):
    def __init__(self, name, email, password, admin_id):
        super().__init__(name, email, password)
        self.admin_id = admin_id


    def create_course(self, course):
        print(f"Course {course} created.")

class TeachingAssistant(Student):
    def __init__(self, name, email, password, student_id, teacher_id):
            Student.__init__(self, name, email, password, student_id)
            Teacher.__init__(self, name, email, password, teacher_id)


    def assist_course(self, course):
        print(f"{self.name} is assisting {course}")



student1 = Student("Nurbolot", "Nurbolot@gmail.com", "02123", "S001")
student1.login()
student1.enroll_in_course("Backend")





admin1 = Admin("Admin", "admin@gmail.com", "admin123", "A001")
admin1.login()
admin1.create_course("Physics")

ta1 = TeachingAssistant("Alex", "alex@gmail.com", "alex123", "S002", "T002")
ta1.login()
ta1.enroll_in_course("Computer Science")
ta1.assist_course("Physics")





    
