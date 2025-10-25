# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Employee.empCount += 1
#     def showCount(self):
#         print(f"Total Employee: {Employee.empCount}")
#     counter = classmethod(showCount)

# e1 = Employee("David", 24)
# e2 = Employee("John", 27)
# e3 = Employee("Jenny", 33)

# e1.showCount()
# Employee.counter()

# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Employee.empCount += 1

#     @classmethod
#     def showCount(cls):
#         print(f"Employee Number: {cls.empCount}")

#     @classmethod
#     def newEmployee(cls, name, age):
#         return cls(name, age)
    
# e1 = Employee("Bhavana", 24)
# e2 = Employee("Rajesh", 26)
# e3 = Employee("John", 27)
# e4 = Employee.newEmployee("Anil", 21)

# Employee.showCount()

# class Cloth:
#     price = 4000
#     @classmethod
#     def showPrice(cls):
#         return cls.price

# print(Cloth.showPrice())

# class Cloth:
#     pass

# @classmethod
# def brandName(cls):
#     print("Name of the brand is Raymond")

# setattr(Cloth, "brand_name", brandName)
# newObj = Cloth()
# newObj.brand_name()

class Cloth:
    @classmethod
    def brandName(cls):
        print("Name of the brand is Raymond")
del Cloth.brandName
print("Method deleted")

