# class Parent:
#     def myMethod(self):
#         print("calling parent method")

# class Child(Parent):
#     def myMethod(self):
#         print("calling child method")
# c = Child()
# c.myMethod()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    
class SalesOfficer(Employee):
    def __init__(self, name, salary, incentives):
        super().__init__(name, salary)
        self.incentives = incentives
    def get_salary(self):
        return self.salary + self.incentives
    
e1 = Employee("Rajesh", 9000)
print("Total salary for {} is Rs.{} ".format(e1.get_name(), e1.get_salary()))
e2 = SalesOfficer("John", 34500, 1200)
print(f"{e2.get_name()} - {e2.get_salary()}")
        