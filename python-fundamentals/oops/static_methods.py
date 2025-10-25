# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Employee.empCount += 1

#     def showCount():
#         print(f"Total Employee: {Employee.empCount}")
#         return
#     counter = staticmethod(showCount)
    
# e1 = Employee("Bhavana", 24)
# e2 = Employee("Rajesh", 26)
# e3 = Employee("John", 27)

# e1.counter()
# Employee.counter()

class Student:
    stdCount = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.stdCount += 1

    @staticmethod
    def showCount():
        print(f"Total Student: {Student.stdCount}")

e1 = Student("Karim", 23)
e2 = Student("Rahim", 26)
e3 = Student("Shumi", 26)
print("Number of Students: ")
Student.showCount()

