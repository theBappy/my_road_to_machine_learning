# class Parent:
#     def parentMethod(self):
#         print("calling parent method")

# class Child(Parent):
#     def childMethod(self):
#         print("calling child method")
# c = Child()
# c.childMethod()
# c.parentMethod()

# class division:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def divide(self):
#       return self.n/self.d
# class modulus:
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def mod_divide(self):
#       return self.n%self.d
      
# class div_mod(division,modulus):
#    def __init__(self, a,b):
#       self.n=a
#       self.d=b
#    def div_and_mod(self):
#       divval=division.divide(self)
#       modval=modulus.mod_divide(self)
#       return (divval, modval)
    
# x = div_mod(10, 3)
# print(f"division: {x.divide()}")
# print(f"mod_division: {x.mod_divide()}")
# print(f"divmod: {x.div_and_mod()}")

# class Universe:
#     def universeMethod(self):
#         print("I am in the universe")
    
# class Earth(Universe):
#     def earthMethod(self):
#         print("I am on the earth")

# class USA(Earth):
#     def USAMethod(self):
#         print("I am in USA")

# person = USA()

# person.universeMethod()
# person.earthMethod()
# person.USAMethod()

# class Manager:
#     def managerMethod(self):
#         print("I am the manager")
# class Employee1(Manager):
#     def employee1Method(self):
#         print("I am a employee-1")
# class Employee2(Manager):
#     def employee2Method(self):
#         print("I am a employee-2")
# emp1 = Employee1()
# emp2 = Employee2()
# emp1.managerMethod()
# emp1.employee1Method()

# class CEO:
#     def ceoMethod(self):
#         print("CEO")

# class Manager(CEO):
#     def managerMethod(self):
#         print("Manager")
    
# class Employee1(Manager):
#     def employee1Method(self):
#         print("Employee-1")

# class Employee2(Manager, CEO):
#     def employee1Method(self):
#         print("Employee-2")

# emp = Employee2()
# emp.ceoMethod()
# emp.managerMethod()
# emp.employee1Method()

class Parent:
    def __init__(self, msg):
        self.msg = msg

    def showMessage(self):
        print(f"Message: {self.msg}")

class Child(Parent):
    def __init__(self, msg):
        super().__init__(msg)

obj = Child("Welcome to leadership")
obj.showMessage()

