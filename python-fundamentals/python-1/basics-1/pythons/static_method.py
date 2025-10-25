# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         Employee.empCount += 1

#     def showCount():
#         print(Employee.empCount)
#         return
#     counter = staticmethod(showCount)

# e1 = Employee("John", 24)
# e2 = Employee("John", 29)
# e3 = Employee("John", 27)

# e1.counter()
# Employee.counter()

class Student:
    stdCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Student.stdCount += 1

    @staticmethod
    def showCount():
        print(Student.stdCount)

s1 = Student("John", 25)
s1 = Student("Jenny", 26)
s1 = Student("David", 29)
print("Number of students: ")
Student.showCount()