# class Employee:
#     'Common base class for all employees'
#     def __init__(self, name, age):
#         self.name = "John"
#         self.age = 24

# e1 = Employee()
# print(f"Name: {e1.name}")
# print(f"Name: {e1.age}")

# class Employee:
#     def __init__(self, name="John", age=23):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         print(f"Employee-Info: {self.name} - {self.age}")

# e1 = Employee()
# e2 = Employee("Jenny", 33)


# print(getattr(e1, "name"))
# print(getattr(e2, "age"))
# print(hasattr(e2, "name"))
# print(setattr(e2, 'salary', 2000))
# print(delattr(e1, "name"))
# e1.salary = 7000
# # print(f"Employee-1 {e1.name} - {e1.age}")
# # print(f"Employee-2 {e2.name} - {e2.age}")
# e1.get_info()
# e2.get_info()
# # print(f"{e1.salary}")
# del e1.salary
# print(f"{e1.salary}")

'''Overloading Constructor'''
class Student:
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.name = args[0]
        elif len(args) == 2:
            self.name = args[0]
            self.age = args[0]
        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]

st1 = Student("John")
print(f"{st1.name}")
st2 = Student("Jenny", 23, "Female")
print(f"{st2.gender}")