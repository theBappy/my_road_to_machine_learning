# class Employee:
#     empCount = 0
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#         Employee.empCount += 1
#     def showCount(self):
#         print(f"{self.empCount}")

#     counter = classmethod(showCount)
# e1 = Employee("John", 24)
# e2 = Employee("Jenny", 26)
# e3 = Employee("David", 27)

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
#         print(f"{cls.empCount}")

#     @classmethod
#     def newEmployees(cls, name, age):
#         return cls(name, age)
    
# e1 = Employee("John", 32)
# e1 = Employee("David", 35)
# e1 = Employee("Kim", 29)
# e1 = Employee("Elise", 27)

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

# class Cloth:

#     @classmethod
#     def brandName(cls):
#         print("Name of the brand is Raymond")
# del Cloth.brandName
# print("Method deleted")