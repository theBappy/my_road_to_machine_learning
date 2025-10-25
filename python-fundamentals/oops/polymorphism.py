
'''Duck Typing'''
class Duck:
    def sound(self):
        return "Quack, Quack!"
    
class AnotherBird:
    def sound(self):
        return "I'm a similar to a duck"
    
def makeSound(duck):
    print(duck.sound())

duck = Duck()
anotherBird = AnotherBird()
makeSound(duck)
makeSound(anotherBird)

'''Method Over-riding'''
from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def draw(self):
        "Abstract method"
        return
class circle(shape):
    def draw(self):
        super().draw()
        print("Draw a circle")
        return
class rectangle(shape):
    def draw(self):
        super().draw()
        print("Draw a rectangle")
        return
    
shapes = [circle(), rectangle()]
for shape in shapes:
    shape.draw()

'''Operator Over-loading'''
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return "Vector (%d %d)" % (self.a, self.b)
    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
    
v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)

'''Method Over-loading'''
def add(*nums):
    return sum(nums)
result1 = add(10, 25)
result2 = add(10, 25, 35)
print(result1)
print(result2)

