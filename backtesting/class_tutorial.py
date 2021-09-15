'''first example'''
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         print(self.name)
#
#     def add_one(self, x):
#         return x + 1
#
#     def bark(self):
#         print("bark")
#
# d = Dog("Tim")
# print(d.add_one(4))
# d.bark()
# print(type(d))

'''second example'''
# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def get_grade(self):
#         return self.grade
#
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
#
# s1 = Student("Tim", 19, 95)
# s2 = Student("Bill", 19, 75)
# s3 = Student("Jill", 19, 65)
#
# course = Course("Science", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.students[0].name)
# print(course.get_average_grade())

'''third example'''
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#     def speak(self):
#         print("I don't know what I say")
#
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name, age) #this is trying to bring attributes from the Pet class over without having to retype everything, and at the same time declaring new attributes for this class
#         self.color = color
#     def speak(self):
#         print("Meow")
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
#
# class Dog(Pet):
#     def speak(self):
#         print("Bark")
#
# class Fish(Pet):
#     pass
#
# p = Pet("Tim", 19)
# p.speak()
# c = Cat("Bill", 34, "Brown")
# c.speak()
# c.show()
# d = Dog("Jill", 34)
# d.speak()
# f = Fish("Bubbles", 10)
# f.speak()

'''fourth example'''
class Person:
    number_of_people = 0 #this is a class attribute

    #this is attribute
    def __init__(self, name):
        self.name = name
#p1 and p2 are object or instance of the Person class
p1 = Person("Tim")
p2 = Person("Jill")

Person.number_of_people = 8
print(p1.number_of_people)
p1.number_of_people = 6
print(p2.number_of_people) #notice that the p2 follow the class attributes declared by the class