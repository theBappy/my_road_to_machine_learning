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
    def set_age(self, age):
        self.__age = age

    name = property(get_name, set_name, "name")
    age = property(get_age, set_age, "age")

e1 = Employee("John", 33)
print(f"{e1.name} - {e1.age}")
e1.name = "Jenny"
e1.age = 35
print(f"{e1.name} - {e1.age}")


# print("------------Getter------------")
# e1 = Employee("John", 24)
# print(f"e1: {e1.get_name()} - {e1.get_age()}")

# # after setting new value
# print("---------After setter------------")
# e1.set_name("Jenny")
# e1.set_age(34)
# print(f"e1: {e1.get_name()} - {e1.get_age()}")


