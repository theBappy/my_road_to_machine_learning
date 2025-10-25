class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")

    
class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Scooby")
cat = Cat("Muffin")
mouse = Mouse("Mickey")

print(dog.name)
print(dog.is_alive)
dog.sleep()
dog.eat()
dog.speak()
cat.speak()
mouse.speak()


class Mobile:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def video(self):
        print(f"{self.model} has video option")
    def audio(self):
        print(f"{self.model} has high-quality sound effects")
    def camera(self):
        print(f"{self.model} has 128mb camera")
    def ram(self):
        print(f"{self.model} has 256gb ram")

class Apple(Mobile):
    def ask_price(self):
        print(f"{self.model} price is 100K")

class Samsung(Mobile):
    def ask_price(self):
        print(f"{self.model} price is 50K")


