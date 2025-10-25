class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("rabbit-1")
hawk = Hawk("hawk-1")
fish = Fish("fish-1")

rabbit.flee()
fish.flee()
fish.hunt()
hawk.hunt()

print(rabbit.name)
fish.eat()
rabbit.sleep()
hawk.eat()
hawk.sleep()