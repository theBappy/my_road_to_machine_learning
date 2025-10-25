from car import Car, CarMain, Smartphone, Desktop, Parent, Child
    
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

my_car=CarMain("Toyota", 2020, "Green", False)
your_car = CarMain("Mercedes", 2005, "Orange", True)

# print(your_car.model)
# print(your_car.year)
# print(your_car.color)
# print(your_car.for_sale)
# my_car.stop()
# my_car.drive()
# my_car.describe()
# your_car.drive()
# your_car.stop()
# your_car.describe()

# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)
# car2.drive()
# car2.stop()

# car2.describe()

# phoneObj = Smartphone("Smartphone", "Samsung")
# print(phoneObj.description())

# desktopObj = Desktop()
# print(desktopObj.sell())

# desktopObj.__max_price = 35000
# print(desktopObj.sell())

# desktopObj.set_max_price(35000)
# print(desktopObj.sell())

# c = Child()
# c.childMethod()
# c.parentMethod()
# c.setAttr(200)
# c.getAttr()
# print(Child().issubclass(Parent))