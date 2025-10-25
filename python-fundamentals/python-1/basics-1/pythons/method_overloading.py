# class example:
#     def add(self, a, b):
#         x = a + b
#         return x
#     def add(self, a, b, c):
#         x = a + b + c
#         return x
# obj = example()
# print(obj.add(10, 20, 30))
# print(obj.add(10, 20)) # shows missing 1 required positional arguments error

# class Example:
#     def add(self, a = None, b = None, c = None):
#         x = 0
#         if a != None and b != None and c != None:
#             x = a + b + c
#         elif a != None and b != None and c == None:
#             x  = a + b
#         return x
# obj = Example()

# print(obj.add(1,2,3))
# print(obj.add(1,2))
from multipledispatch import dispatch

class example:
    @dispatch(int, int)
    def add(self, a, b):
        x = a + b
        return x
    @dispatch(int, int, int)
    def add(self, a, b, c):
        x = a + b + c
        return x
obj = example()
print(obj.add(10, 20, 30))
print(obj.add(10, 20))