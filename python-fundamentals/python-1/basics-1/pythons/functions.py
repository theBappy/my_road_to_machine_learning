# def greetings():
#     "This is docstring of greeting function"
#     print("Hello World")
#     return
# greetings()

# def printme(str):
#     print(str)
#     return
# printme("Good Morning")

# def testFunction(arg):
#     print("ID inside the function", id(arg))
# var = "Hello"
# print("ID before passing", id(var))
# testFunction(var)

# def testFunction(arg):
#     print("ID inside the function", id(arg))
#     arg = arg + 1
#     print("New object after increment", arg, id(arg))
# var = 10
# print("ID before passing: ", id(var))
# testFunction(var)
# print("Value after function call: ", var)

# def testFunction(arg):
#     print("Inside function: ", arg)
#     print("ID inside the function: ", id(arg))
#     arg = arg.append(100)

# var = [10, 20, 30, 40]
# print("ID before passing: ", id(var))
# testFunction(var)
# print("List after function call: ", var)

# def greetings(name):
#     "This is docstring of greetings function"
#     print("Hello {}".format(name))
#     return
# greetings("Jenny")
# greetings("Stephen")
# greetings("John")

# def printme(str):
#     "This is a passed string into this function"
#     print(str)
#     return
# printme()

# def printme(str):
#     "This prints a passed string into this function"
#     print(str)
#     return
# printme(str = "My World")

# def printInfo(name, age):
#     print("Name: ", name)
#     print("Age: ", age)
#     return
# printInfo(age = 50, name ="John")

# def printInfo(name, age = 35):
#     print("Name: ", name)
#     print("Age: ", age)
#     return
# printInfo(age = 50, name="John")
# printInfo(name="Jenny")

# def posFun(x, y, /, z):
#     print(x + y + z)
# print("Evaluating positional-only arguments")
# posFun(33, 22, z=11)

# def posFunc(*, num1, num2, num3):
#     print(num1 * num2 * num3)
# print("Evaluating keyword-only arguments: ")
# posFunc(num1=6, num2=8, num3=5)

# def printInfo(arg1, *vartuple):
#     print("Output is: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# printInfo(10)
# printInfo(70, 60, 50)
# def add(x, y):
#     z = x + y
#     return z
# a = 10
# b = 20
# result = add(a,b)
# print("a = {} b = {} a + b ={}".format(a,b, result))

# sum = lambda arg1, arg2: arg1 + arg2
# print(sum(10, 20))

# sum = lambda a, b: a + b
# print(sum(10,20))

# multiplication = lambda num1, num2 : num1 * num2
# print(multiplication(4, 5))

# total = 0
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Inside the function local total: ", total)
#     return total
# sum(10, 20)
# print("Outside the function global total: ", total)
