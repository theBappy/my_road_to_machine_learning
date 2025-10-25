# class Parent:
#     def parentMethod(self):
#         print("Calling parent method")

# class Child(Parent):
#     def parentMethod(self):
#         print("Calling child method by over riding parent method")
# c = Child()
# c.parentMethod()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getName(self):
        return self.name
    
    def getSalary(self):
        return self.salary
    
class SalesOfficer(Employee):
    def __init__(self, name, salary, incentives):
        super().__init__(name, salary)
        self.incentives = incentives

    def getSalary(self):
        return self.salary + self.incentives
    
e1 = Employee("Rajesh", 9000)
print(f"{e1.getName()} => {e1.getSalary()}")

e2 = SalesOfficer("Kiran", 10000, 1200)
print(f"{e2.getName()} => {e2.getSalary()}")