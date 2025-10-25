# class Employee:
#     name = "John Doe"
#     age = "30"

# emp = Employee()
# print("Name: ", emp.name)
# print("Age: ", emp.age)

# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         Employee.empCount += 1
#         print(f"Name: {self.__name}, Age: {self.__age}")
#         print("Employee count: ", Employee.empCount)

# e1 = Employee("John", 21)
# print()

# class Employee:
#     def __init__(self, name="John", age = 24):
#         self.name = name
#         self.age = age
#     def displayEmployee(self):
#         print(f"Name: {self.name} - Age: {self.age}")
# print("Employee.__doc__: ",Employee.__doc__)
# print("Employee.__name__: ", Employee.__name__)
# print("Employee.__module__: ", Employee.__module__)
# print("Employee.__bases__: ", Employee.__bases__)
# print("Employee.__dict__: ", Employee.__dict__)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        print(f"Name: {self.name} - Grade: {self.grade}")

student1 = Student("Ram", "B")
student2 = Student("Sham", "C")