# Inheritance = allows a class to inherit attributes and methods from another class, helps with code reusability and extensibility class Child(Parent) 
# Animal -> Dog, Cat, Mouse

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
        print(f"WOOF!")

class Cat(Animal):
    def speak(self):
        print(f"MEOW!")

class Mouse(Animal):
    def speak(self):
        print(f"SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Shinjo")
mouse = Mouse("Mickey")

print(mouse.name)
print(mouse.is_alive)

mouse.eat()
mouse.sleep()
dog.speak()
cat.speak()
mouse.speak()