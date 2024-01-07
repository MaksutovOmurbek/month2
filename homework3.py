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

student = Student("Nurbolot", "Nurbolot@gmail.com", "02123", "S001")
student.login()
student.enroll_in_course("Backend")

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

class TeacherAssistant(Student):
    def __init__(self, name, email, password, student_id, teacher_id):
            Student.__init__(self, name, email, password, student_id)
            Teacher.__init__(self, name, email, password, teacher_id)


    def assist_course(self, course):
        print(f"{self.name} is assisting {course}")



student = Student("Nurbolot", "Nurbolot@gmail.com", "02123", "S001")
student.login()
student.enroll_in_course("Backend")





admin = Admin("Admin", "admin@gmail.com", "admin123", "A001")
admin.login()
admin.create_course("Physics")

teach = TeacherAssistant("Alex", "alex@gmail.com", "alex123", "S002", "T002")
teach.login()
teach.enroll_in_course("Computer Science")
teach.assist_course("Physics")





    
