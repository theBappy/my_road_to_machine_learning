# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self):
#         print(f"You drive the {self.color} {self.model}")
#     def stop(self):
#         print(f"You stop the {self.color} {self.model}")

#     def describe(self):
#         print(f"{self.year} {self.color} {self.model}")



# class CarMain:
#     def __init__(self,  model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
#     def drive(self):
#         print(f"You drive the {self.color} - {self.color}")
#     def stop(self):
#         print(f"You stop the {self.color} - {self.model}")
#     def describe(self):
#         print(f"{self.model} - {self.year} - {self.for_sale}")

# class Smartphone:
#     def __init__(self, device, brand):
#         self.device = device
#         self.brand = brand

#     def description(self):
#         return f"{self.device} of {self.brand} supports Android 14"
    

# class Desktop:
#     def __init__(self):
#         self.__max_price = 25000
#     def sell(self):
#         return f"Selling price: {self.__max_price}"
#     def set_max_price(self, price):
#         if price > self.__max_price:
#             self.__max_price = price

# class Parent:
#     parentAttr = 100
#     def __init__(self):
#         print("Calling parent constructor")

#     def parentMethod(self):
#         print("Calling parent method")

#     def setAttr(self, attr):
#         Parent.parentAttr = attr

#     def getAttr(self, attr):
#         print("Parent attribute: ", Parent.parentAttr)

# class Child:
#     def __init__(self):
#         print("Calling child constructor")
#     def childMethod(self):
#         print("Calling child method")

# class Vector:
#     def __init__(self, a, b):
#         self.a = a 
#         self.b = b

#     def __str__(self):
#         return "Vector (%d, %d)" % (self.a, self.b)
#     def __add__(self, other):
#         return Vector(self.a + other.a, self.b + other.b)
    
# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)


class Employee:
    "Common base class for all employees"
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

print("Employee.__doc__: ", Employee.__doc__)
print("Employee.__name__: ", Employee.__name__)
print("Employee.__module__: ", Employee.__module__)
print("Employee.__bases__: ", Employee.__bases__)
print("Employee.__dict__: ", Employee.__dict__)

# emp1 = Employee("John", 20000)
# emp2 = Employee("Mark", 20000)

# emp1.displayEmployee()
# emp2.displayEmployee()
# emp1.age = 7
# emp2.age = 8
# print(hasattr(emp1, 'age'))
# print(getattr(emp1, 'age'))
# setattr(emp1,'age', 27)
# print(hasattr(emp1, 'age'))
# print(getattr(emp1, 'age'))
# delattr(emp1, 'age')
# print(hasattr(emp1, 'age'))
# print("Total Employee %d" % Employee.empCount)

num= 20
print(type(num))
num1=90.90
print(type(num1))
s = "hello"
print(type(s))
dct = {'a': 1, 'b': 2, 'c':3}
print(type(dct))
def sayHello():
    print("Hello world")
    return
print(type(sayHello))


a = 40
b = a
c = [b]
del a
b = 100
c[0] =-1

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")
pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter.__secretCount)



    


