class Student:
    def __init__(self, name, roll_no, course, age):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Age:", self.age)


class Employee:
    def __init__(self, emp_id, name, dept, salary):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
        self.salary = salary

    def display(self):
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Salary:", self.salary)


class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def drive(self):
        print(self.brand, self.model, "is driving...")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name, "Age:", self.age)


class StudentPerson(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

    def show_info(self):
        super().show_info()
        print("Roll No:", self.roll_no)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print("Subject:", self.subject)


s1 = Student("Abdullah", "2025-CE-01", "Computer Engineering", 20)
s2 = Student("Ali", "2025-CE-02", "Software Engineering", 21)
s1.display()
s2.display()

e1 = Employee("101", "Sara Khan", "IT", 150000)
e2 = Employee("102", "Usman Ahmed", "HR", 120000)
e1.display()
e2.display()

c1 = Car("Toyota", "Corolla", 6500000)
c2 = Car("Honda", "Civic", 8500000)
c1.drive()
c2.drive()

p1 = Person("Tariq", 45)
p1.show_info()

sp1 = StudentPerson("Hamza", 22, "103")
sp1.show_info()

t1 = Teacher("Dr Hassan", 48, "Computer Science")
t1.show_info()
