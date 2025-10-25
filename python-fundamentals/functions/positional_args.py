# def add(x, y):
#     z = x + y
#     print("x={} y={} z={}".format(x, y, z))
# add(13, 12)

# def add(x, y):
#     z = x + y
#     print(z)
# a = 10
# add(a)

# def add(x, y):
#     z = x + y 
#     print(z)

# add(2,3,4)

# def add(x, y):
#     z = x + y
#     print(z)
# a = "Hello"
# b = 10
# add(a,b)

# name = input(prompt = "Enter your name")

# def intr(amount, rate, /):
#     val = amount * rate / 100
#     return val
# print(intr(316200, 2))

# def intr(amount, rate, /):
#     val = amount * rate / 100
#     return val
# print(intr(amount = 1000, rate=10))

def myfunction(x, /, y, *, z):
    print(x, y, z)
myfunction(10, y = 20, z = 30)
