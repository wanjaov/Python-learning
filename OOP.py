# """
# OOP (Object Oriented Programming)

# Pillars of OOP
# 1. Abstraction
# 2.Polymorphism
# 3.Inheritance
# 4.Encapsulation

# Class - A blueprint from which an object can be created
# Object - This is an instantiation of a class
# Constructor - A constructor helps to create objects from a class
#  NB: Creating classes involve using the pascal case.
#  Method: A function that belongs to a particular class
#  Attribute: A variable defined inside a class (that belongs to  that class)
# """

# #DEFINING A CLASS
# class Animal:
#     def __init__(self):
#         pass
#     name = "lion"
#     group = "Carnivorous"
#     sound = "Roars"


# animal = Animal()

# print(animal.name)
# print(animal.group)
# print(animal.sound)

# animal.sound="Brays"
# print(animal.sound)

# #How to create a method in a class, replace the sound attribute with a method 

# """
# OOP(Object Oriented Programming)

# Pillars of OOP
# 1. Abstraction
# 2. Polymorphism
# 3. Inheritance
# 4. Encapsulation

# Class - A blueprint from which an object can be created
# Object - This is an instantiation of a class
# Constructor - A constructor helps us to create objects from 
# a class

# NB: Creating classes involves using the Pascal case.

# Method: A function that belongs to a particular class
# Attribute: A variable defined inside a class(that belongs to that class)
# """

# # defining a class
# class Animal:
#     # Constructor
#     def __init__(self):
#         self.name = "lion"
#         self.group = "Carnivorous"

#     def sound_animal(self):
#         return "Roars"
    
#     def character(self):
#         return "Brave"


# animal = Animal()

# print(animal.name)
# print(animal.group)
# print(animal.sound_animal())
# print(animal.character())

# # TODO How to create a method in a class, replace the sound attribute with a method

# class Calculator:
#     def __init__(self, x: int, y: int):
#         self.x_value = x
#         self.y_value = y
    
#     def get_x(self):
#         return self.x_value

#     def get_y(self):
#         return self.y_value
    
#     def add(self):
#         return self.x_value + self.y_value
    
#     # TODO Provide multiplication, division, modulus
    
    # def multiplication(self):
    #     return self.x_value * self.y_value    
    
    # def division(self):
    #     return self.x_value / self.y_value
    
    # def modulus(self):
    #      return self.x_value % self.y_value


# calculator = Calculator(6,7)

# print(calculator.get_x())
# print(calculator.get_y())
# print(calculator.add())
# print(calculator.multiplication())
# print(calculator.division())
# print(calculator.modulus())

# calculator2 = Calculator(7,8)

# print(calculator2.get_x())
# print(calculator2.get_y())
# print(calculator2.add())
# print(calculator2.multiplication())
# print(calculator2.division())
# print(calculator2.modulus())


""" 
ENCAPSULATION
- This is a concept that helps us regulate accessibility to attributes and methods
- We can implement read only permissions, write only permissions and read and write permissions on attributes

We do this by using some characteristics on our methods and attributes eg:
1. private: This is where an attribute/method is only accessible from inside the class, otherwise it cannot be accessed outside the class. i.e even
when instatiating its own object.
2. public: This is where an attribute or method is accessible when we instantiate its object
* TODO 3. protected(C++)
"""

class User:
    def __init__(self, national_id, email, first_name, last_name):
        # Making a private attribute we use two underscores before the name of our attribute
        self.__national_id_value = national_id
        self.email_value = email
        self.first_request = first_name
        self.last_request = last_name
    
    # Making private methods: we use two underscores before the name of our method
    def __private_method_example(self):
        return "Testing this method"
    
    def get_national_id_value(self):
        return self.__national_id_value
    
    def get_email_value(self):
        return self.email_value
    
    def get_first_request(self):
        return self.first_request
    
    def get_last_request(self):
        return self.last_request
    
    
    def set_national_id(self, new_national_id):
        self.__national_id_value = new_national_id

    def set_national_id(self, new_national_id):
        self.set_national_id_value = new_national_id
  
    def set_email(self, new_email):
       self.set_email_value = new_email
  
    def set_first_name(self, new_first_name):
        self.set_first_request = new_first_name
  
    def set_last_name(self, new_last_name):
        self.set_last_request = new_last_name
  
    
    
user = User(123456, "wanjaov@gmail.com", "Victor", "Wanjao")


print(user.get_national_id_value())
user.set_national_id(10010011)
print(user.get_national_id_value())

# TODO Make email a private attribute, generate its setter, generate setters for all other attributes of the class User(first_name, last_name)

"""
Inheritance
-This is where a class obtains te properties (attributes and methods) of another class, it helps reduce redundancies
I.E:Class B can inherit the properties of a class A, how we represent this code is:
class B(A):
    # class properties here
"""
class Employee(User):
    def __init__(self, national_id, email, first_name, last_name, company_title):
        super().__init__(national_id, email, first_name, last_name)
        self.company_title = company_title

    def get_company_title(self):
        return self.company_title
    
    def set_company_title(self, new_company):
        self.company_title = new_company

employee = Employee(90010011, "delivce@gmail.com", "Albert", "Njenga", "Safaricom")

print(employee.get_national_id_value())
print(employee.get_email_value())
print(employee.get_company_title())
print(employee.get_first_request())
print(employee.get_last_request())

# TODO Create a student that inherits from User, and has the extra fields registretion_no, course and department, create their respective getters and setters too

class Student(User):
    def __init__(self, national_id, email, first_name, last_name, registration_no, course, department):
        super().__init__(national_id, email, first_name, last_name)
        self.registration_no = registration_no
        self.course = course
        self.department = department

    def get_registration_no(self):
        return self.registration_no
    
    def set_registration_no(self, new_registration):
        self.registration_no = new_registration

    def get_course(self):
        return self.course
    
    def set_course(self, new_course):
        self.course = new_course

    def get_department(self):
        return self.department
    
    def set_department(self, new_department):
        self.department = new_department

student = Student(9000234, "delive@gmail.com", "kamau", "Njenga", "81-5019/2023", "Software", "Developer")

print(student.registration_no)
print(student.course)
print(student.department)

# Class Lecturer: school(string), department(string), units(list)

class Lecturer(User):
    def __init__(self, national_id, email, first_name, last_name, school: str, department: str, unit: list):
        super().__init__(national_id, email, first_name, last_name)
        self.school = school
        self.department = department
        self.unit = unit

    def get_school(self):
        return self.school
    
    def set_school(self, new_school):
        self.school = new_school

    def get_department(self):
        return self.department
    
    def set_department(self, new_department):
        self.department = new_department

    def get_unit(self):
        return self.unit
    
    def set_unit(self, new_unit):
        self.unit = new_unit

lecturer = Lecturer(90000100, "deelive@gmail.com", "Kamau", "Njenga", "Muvatech", "Developer", '[Object oriented, Basic Math, Communication skills]')

print(lecturer.school)
print(lecturer.department)
print(lecturer.unit)

#TODO Go read about abstract classes in python and how we use them, come up with your own examples





  
  









