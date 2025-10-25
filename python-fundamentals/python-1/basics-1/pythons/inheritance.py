# class Parent:
#     def parentMethod(self):
#         print("Calling parent method")
    
# class Child(Parent):
#     def childMethod(self):
#         print("Calling child method")
# c = Child()
# c.childMethod()
# c.parentMethod()

# class Division:
#     def __init__(self, a, b):
#         self.n = a
#         self.d = b
#     def divide(self):
#         return self.n / self.d
# class Modulus:
#     def __init__(self, a, b):
#         self.n = a
#         self.d = b
#     def mod_divide(self):
#         return self.n % self.d
    
# class div_mod(Division, Modulus):
#     def __init__(self, a, b):
#         self.n = a
#         self.d = b
#     def div_and_mod(self):
#         div_val = Division.divide(self)
#         mod_val = Modulus.mod_divide(self)
#         return (div_val, mod_val)
    
# x = div_mod(10,3)
# print("Division: ", x.divide())
# print("Mod_Division: ", x.mod_divide())
# print("Div_Mod_Division: ", x.div_and_mod())

# Method Resolution Order(MRO)

# Multi-Level Inheritance
# class Universe:
#     def universeMethod(self):
#         print("I am in the Universe")
    
# class Earth(Universe):
#     def earthMethod(self):
#         print("I am on Earth")

# class USA(Earth):
#     def USAMethod(self):
#         print("I am in USA")

# country = USA()
# country.universeMethod()
# country.earthMethod()
# country.USAMethod()

# Hierarchial Inheritance
# class Manager:
#     def managerMethod(self):
#         print("Manager")
# class Employee1(Manager):
#     def employee1Method(self):
#         print("Employee 1")
# class Employee2(Manager):
#     def employee2Method(self):
#         print("Employee 2")

# emp1 = Employee1()
# emp2 = Employee2()

# emp1.managerMethod()
# emp1.employee1Method()
# emp2.managerMethod()
# emp2.employee2Method()

# Hybrid Inheritance
# Combination of two or more types of inheritance

# class CEO:
#     def ceoMethod(self):
#         print("CEO")
# class Manager(CEO):
#     def managerMethod(self):
#         print("Single inheritance - Manager from CEO")
# class Emp1(Manager):
#     def emp1Method(self):
#         print("Single inheritance - Emp1 from Manager")
# class Emp2(Manager, CEO):
#     def emp2Method(self):
#         print("Multiple inheritance - Emp2 from both CEO & Manager")

# emp = Emp2()
# emp.managerMethod()
# emp.ceoMethod()
# emp.emp2Method()

class Parent:
    def __init__(self, msg):
        self.message = msg
    def showMessage(self):
        print(self.message)

class Child(Parent):
    def __init__(self, msg):
        super().__init__(msg)
obj = Child("Welcome to python era")
obj.showMessage()


