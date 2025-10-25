# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) -> Local -> Enclosed -> Global -> Built-In

# def func1():
#     x = 1
#     def func2():
#         # x = 2
#         print(x)
#     func2()

# func1()

# def func1():
#     # x = 1
#     print(x)

# def func2():
#     # x = 3
#     print(x)
# x = 5

# func1()
# func2() 

from math import e

# print(e)

def func1():
    print(e)

e = 3
func1()