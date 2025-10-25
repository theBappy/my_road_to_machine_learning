# def function_name(parameters):
#     "function_docstring"
#     function_suite
#     return [expression]

# def greetings():
#     "this is docstring of greetings function"
#     print("Hello world")
#     return
# greetings()

# def printme(str):
#     "this prints a passed string into this function"
#     print(str)
#     return

# printme("hello")
# printme("john")


# def testFunction(arg):
#     print("id inside the function: ", id(arg))
# var = "hello"
# print("id before passing: ", id(var))
# testFunction(var)

# def testFunction(arg):
#     print("id inside the function: ", id(arg))
#     arg = arg + 1
#     print("new object after increment: ", arg, id(arg))

# var = 10
# print("id before passing: ", id(var))
# testFunction(var)
# print("value after function call: ",var)

# def testFunction(arg):
#     print("inside function: ", arg)
#     print("id inside the function: ", id(arg))
#     arg = arg.append(100)

# var = [10, 20, 30, 40]
# print("id before passing : ", id(var))
# testFunction(var)
# print("list after function call: ", var)


# def greetings(name):
#     "this is docstring of greetings function"
#     print("Hello {}".format(name))
#     return
# greetings("John")
# greetings("Rose")


# def printme(str):
#     print(str)
#     return
# printme()

# def greetings(name, age):
#     print(f"Happy {age}'th birthday, {name}!")
#     return 
# greetings(age = 23, name = "Jenny")

# def printInfo(name, age = 35):
#     print("Name: ", name)
#     print("Age: ", age)
#     return
# printInfo(age = 50, name = "John")
# printInfo(name = "David")


# def posFn(x, y, /, z):
#     print(x + y + z)
# posFn(33, 22, z=11)

# def keyFn(*, num1, num2, num3):
#     print(num1 * num2 * num2)
# keyFn(num2=3,num3=4,num1=2)

# def printInfo(arg1, *vartuple):
#     print("Output is: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
# print(10)
# print(10, 20)
# print(10, 20, 30, 40)

# def add(x,y):
#     z = x + y
#     return z
# a = 10
# b = 20
# result= add(a, b)
# print(result)

# sum = lambda arg1, arg2 : arg1 + arg2
# print(sum(10, 20))

# total = 0
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print("inside the function local total: ", total)
#     return total
# sum(10, 20)
# print("outside the function global total: ", total)

def percent(phy, maths, maxmarks = 200):
    val = (phy + maths) * 100 /maxmarks
    return val

# phy = 60
# maths = 70
# result = percent(phy, maths)
# print("percentage: ", result)

# phy = 60
# maths = 70
# result = percent(60, 70, 100)
# print(result)






