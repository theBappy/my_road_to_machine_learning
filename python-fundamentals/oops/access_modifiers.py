# class Employee:
#     def __init__(self, name="John", age = 23):
#         self.name = name 
#         self.age = age
# e1 = Employee()
# e2 = Employee("Jenny", 34)

# print(f"Emp-1: {e1.name} - {e1.age}")
# print(f"Emp-2: {e2.name} - {e2.age}")


# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.__age = age
#         self._salary = salary
#     def displayEmployee(self):
#         print(f"Name: {self.name}\n, Age: {self.__age}\n, Salary: {self._salary}")
# e1 = Employee("John", 24, 15500)
# print(e1.name)
# print(e1._salary)
# print(e1.__age)
# print(e1._Employee__age)
# print(e1._Employee__age)
# print(e1._Employee__age)
# print(e1._Employee__age)
# print(e1._Employee__age)

class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, name):
        self.__name = name
        return
    def set_age(self, age):
        self.__age = age
        return
    name = property(get_name, set_name, "name")
    age = property(get_age, set_age, "age")


e1 = Employee("John Doe", 24)
print(f"{e1.name} - {e1.age}")
# print(f"{e1.get_name()} - {e1.get_age()}")
# e1.set_name("Jenny")
# e1.set_age(26)
# print(f"{e1.get_name()} - {e1.get_age()}")
    
