class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print(f"Total employee: {Employee.empCount}")
    def displayEmployee(self):
        print(f"Name: {self.name} - Salary: {self.salary}")

# print(Employee.__doc__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__bases__)
# print(Employee.__dict__)   

# emp1 = Employee("Zara", 2000)
# emp2 = Employee("John", 3000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# emp1.age = 23
# print(emp1.age)
# del emp1.age
# print(getattr(emp1, "name"))
# print(hasattr(emp2, "salary"))
# print(setattr(emp1, "age", 23))
# print(getattr(emp1, "age"))
# del emp1.age
# print(emp1.age)
# print(Employee.displayCount())
# a = 40
# b = a
# c = [b]
# del a
# b = 100
# c[0] =-1

# class Point:
#     def __init__(self, x = 0, y = 0):
#         self.x = x 
#         self.y = y
#     def __del__(self):
#         class_name = self.__class__.__name__
#         print(class_name, "destroyed")

# pt1 = Point()
# pt2 = Point()
# pt3 = pt1
# print(id(pt1), id(pt2), id(pt3))

# del pt1
# del pt2
# del pt3


class JustCounter:
    __secretCounter = 0
    def count(self):
        self.__secretCounter += 1
        print(self.__secretCounter)
counter = JustCounter()
counter.count()
counter.count()
# print(counter.__secretCounter)
print(counter._JustCounter__secretCount)