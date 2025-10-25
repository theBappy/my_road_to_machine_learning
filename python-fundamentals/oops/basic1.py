# class Smartphone:
#     def __init__(self, device, brand):
#         self.device = device
#         self.brand = brand
#     def description(self):
#         return f"{self.device} of {self.brand} supports Android-14"
# phoneObj =Smartphone("Smartphone", "Samsung")
# print(phoneObj.device)
# print(phoneObj.brand)
# print(phoneObj.description())

# class Desktop:
#     def __init__(self):
#         self.__max_price = 25000
#     def sell(self):
#         return f"Selling Price: {self.__max_price}"
#     def set_max_price(self, price):
#         if price > self.__max_price:
#             self.__max_price = price

# desktopObj = Desktop()
# # print(desktopObj.sell())

# desktopObj.__max_price = 35000
# print(desktopObj.sell())

# desktopObj.set_max_price(35000)
# print(desktopObj.sell())

# class Parent:
#     parentAttr = 100
#     def __init__(self):
#         print("Calling parent constructor")
#     def parentMethod(self):
#         print("calling parent method")
#     def setAttr(self, attr):
#         Parent.parentAttr = attr
#     def getAttr(self):
#         print("Parent attribute: ", Parent.parentAttr)

# class Child(Parent):
#     def __init__(self):
#         print("calling child constructor")

#     def childMethod(self):
#         print("calling child method")

# c = Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)
v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)
    