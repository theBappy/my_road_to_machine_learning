
# Abstraction
from abc import ABC, abstractmethod

class demo(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method")
        return
    def method2(self):
        print("concrete method")

class concreteclass(demo):
    def method1(self):
        super().method1()
        return
obj = concreteclass()
obj.method1()
obj.method2()


# Encapsulation
# class Student:
#     def __init__(self, name="John", age=50):
#         self.name = name
#         self.age = age
# s1 = Student()
# s2 = Student("Jenny", 28)
# print(f"s1: {s1.name} - {s1.age}")
# print(f"s2: {s2.name} - {s2.age}")

class Student:
    def __init__(self, name="John", marks=88):
        self.__name = name
        self.__marks = marks

    def studentData(self):
        print(f"Name: {self.__name} - Marks: {self.__marks}")

s1 = Student()
s2 = Student("Jenny", 76)
s1.studentData()
s2.studentData()

# Name Mangling
# Accessing private date in public scope by name mangling
print(f"{s1._Student__name} {s1._Student__marks}")
print(f"{s2._Student__name} {s2._Student__marks}")



