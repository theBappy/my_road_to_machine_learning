# def myFunction():
#     a = 10
#     b = 20
#     print("variable a: ", a)
#     print("variable b: ", b)
#     return a + b
# print(myFunction())

# name = "Tutorial"
# marks = 50
# def myFunc():
#     print("name: ", name)
#     print("marks: ", marks)
# myFunc()

# def myFunction():
#     a = 5
#     b = 6
#     # nested function
#     def nestedFunction():
#         nonlocal a
#         nonlocal b
#         a = 10
#         b = 20
#         print("variable a: ", a)
#         print("variable b: ", b)
#         return a + b
#     print(nestedFunction())
# myFunction()

# print(globals())
# name = 'TutorialsPoint'
# marks = 50
# result = True
# def myfunction():
#    a = 10
#    b = 20
#    c = a+b
#    print ("globals():", globals())
#    print ("locals():", locals())
#    return c
# myfunction()

# print(globals()['name'])
# print(locals().get('a'))

# marks = 50
# def myFunction():
#     marks = marks + 20
#     print(marks)
# myFunction()
# print(marks)

# var1 = 50
# var2 = 60
# def myFunction():
#     "Change values of global variables"
#     globals()['var1'] = globals()['var1'] + 10
#     global var2
#     var2 = var2 + 20

# myFunction()
# print("var1: ", var1, "var2: ", var2)
# var1 = 50
# var2 = 60
# def myFunction(x, y):
#     total = x + y
#     print("Total is a local variable: ", total)
# myFunction(var1, var2)
# print(total)


