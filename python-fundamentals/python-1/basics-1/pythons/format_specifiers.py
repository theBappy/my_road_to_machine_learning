# string interpolation = involving variables and expressions into strings
# print(f"Hello world")
# print(F"Welcome to paris")

# site = "Real Python"
# print(f"Welcome to {site}")

# quantity = 6
# item = 'Bananas'
# price = 1.74
# print(f"The price of {item} is ${price} for {quantity} piece")

# fruits = ["apple", "mango", "banana"]
# numbers = {"one": 1, "two": 2, "three": 3}
# print(f"First fruits is in the list {fruits[0]}")
# print(f"Second fruits is in the list {fruits[1]}")
# print(f"Dict value for key 'one' is {numbers['one']}")

# lang = "Python"
# print(f"{{ {lang} }}")

# lang = "JavaScript"
# print(f"{{{lang}}}")

# lang = "Python"
# print(f"Hello {{{lang}}}")

# print("{0} {1} cost ${2}".format(6, 'bananas', 1.74 * 6))

# print("{0} {1} cost ${2:.2f}".format(3, "Apple", 2.35 * 3))

# print("{quantity} {item} cost ${cost:.2f}".format(
#     quantity = 6,
#     item="Apple",
#     cost = 1.7554 * 6
# ))

# print("{x} {y} {z}".format(
#     x="foo",
#     y="bar",
#     z="kar"
# ))
# x = 'foo'
# y = 'bar'
# z = 'baz'
# print("{0} {1} {s}".format(x, y, s=z))

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"I'm {self.name}, and I'm {self.age} years old"
#     def __repr__(self):
#         return f"{type(self).__name__}(name='{self.name}', age={self.age})"
    
# jane = Person("Jane", 25)
# print(f"{jane!s}")
# print(f"{jane!r}")
# print("{jane!s}".format(jane=jane))
# print("{jane!r}".format(jane=jane))

# print(f"{257:b}")
# print("{:b}".format(257))
# print("{:c}".format(42))
# print(chr(42))
# print(f"{3.14156:g}")
# print(f"{-12344455.09808:g}")