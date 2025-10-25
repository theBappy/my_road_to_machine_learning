# def myFunction(a: int, b: int):
#     c = a + b
#     return c
# print(myFunction(10, 20))
# print(myFunction("Hello", " World"))

# def myFunction(a: int, b: int) -> int:
#     c = a + b
#     return c
# print(myFunction(56, 88))
# # print(myFunction("Hello", " world"))
# print(myFunction.__annotations__)

# def total(x: "marks in physics", y: "marks in chemistry"):
#     return x + y
# print(total(86, 88))
# print(total.__annotations__)

# def myFunction(a: "physics", b: "maths" = 20) -> int:
#     c = a + b
#     return c
# print(myFunction(10))
# print(myFunction.__annotations__)
# print(dir(myFunction))

# def myFunction(a:"physics", b:"maths" = 20) -> int:
#     c = a + b
#     return c
# print(myFunction.__annotations__)

# def myFunction(*args: "arbitrary args", **kwargs: "arbitrary keyword args")-> int:
#     pass
# print(myFunction.__annotations__)

def division(num: dict(type=float, msg="numerator"), den: dict(type=float, msg="denominator")) -> float:
    return num / den
print(division.__annotations__)
