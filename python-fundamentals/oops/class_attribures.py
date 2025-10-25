# class Employee:
#     name = "John Doe"
#     age = 34

# emp = Employee()
# print(Employee.name)

class Employee:

    empCount = 0
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Employee.empCount += 1
        print(f"Name: {self.__name}, Age: {self.__age}")
        print("Employee count: ", Employee.empCount)

e1 = Employee("John", 33)
print()
e2 = Employee("David", 45)
