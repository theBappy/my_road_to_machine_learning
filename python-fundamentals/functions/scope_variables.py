# def myFunction():
#     a = 10
#     b = 20
#     print("variable a: ", a)
#     print("variable b: ", b)
#     return a + b
# print(myFunction())

# name = "TutorialsPoints"
# marks = 50
# def myFunction():
#     print("name: ", name)
#     print("marks: ", marks)
# myFunction()

# def func1():
#     a = 5
#     b = 6
#     def func2():
#         nonlocal a 
#         nonlocal b
#         a = 10
#         b = 20
#         print("variable a: ", a)
#         print("variable b: ", b)
#         return a + b
#     print(func2())
# func1()

# name = "TutorialPoints"
# marks = 20
# result = True
# def myfunction():
#     a = 10
#     b = 20
#     return a + b
# print(globals())

# name ="John Doe"
# marks = 50
# result = True
# def myFunction():
#     a = 10
#     b = 20
#     c = a + b
#     # print("globals(): ", globals())
#     # print("locals(): ", locals())
#     return c
# myFunction()
# print(globals()['name'])
# print(globals()['marks'])
# print(globals()['result'])
# print(locals().get('a'))
# print(locals().get("c"))

# marks = 50
# def myFunction():
#     marks = 70
#     print(marks)
# myFunction()
# print(marks)

# marks = 50
# def myfunction():
#     marks = marks  + 20
#     print(marks)
# myfunction()
# print(marks)

# var1 = 50
# var2 = 60
# def myFunction():
#     "change value of global variables"
#     globals()['var1'] = globals()['var1'] + 10
#     global var2
#     var2 = var2 + 20
# myFunction()
# print("var1: ",var1, "var2: ", var2)
var1 = 50
var2 = 60
def myFunction(x, y):
    global total
    total = x + y
    print("Total is a local variable: ", total)
myFunction(var1, var2)
print(total)