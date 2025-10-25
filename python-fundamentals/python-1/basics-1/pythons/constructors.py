# class Employee:
#     def __init__(self):
#         self.name = "John"
#         self.age = 24

# e1 = Employee()
# print("Name: {}".format(e1.name))
# print("Age: {}".format(e1.age))

# class Employee:
#     def __init__(self, name="Jenny", age=24):
#         self.name = name
#         self.age = age

#     def displayEmployee(self):
#         print(f"Name: {self.name} - Age: {self.age}")

# e1 = Employee()
# e2 = Employee("David", 28)
# e1.age = 27
# e1.name = 'Kim'
# e1.displayEmployee()
# e2.displayEmployee()
# print(hasattr(e1, 'age'))
# print(hasattr(e1, 'salary'))
# print(getattr(e1, 'name'))
# print(getattr(e1, 'age'))
# print(getattr(e2, 'name'))
# print(getattr(e2, 'age'))
# delattr(e1, 'age')
# delattr(e1, 'name')
# print(getattr(e1, 'name'))
# print(f"e1: {e1.name} - {e1.age}")
# print(f"e2: {e2.name} - {e2.age}")

class Student:
    def __init__(self, **args):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.name = args[1]
        elif len(args) == 3:
            self.name = args[0]
            self.name = args[1]
            self.name = args[2]

