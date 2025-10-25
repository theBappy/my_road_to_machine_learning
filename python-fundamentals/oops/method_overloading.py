# class example:
#     def add(self, a = None, b = None, c = None):
#         x = 0
#         if a != None and b != None and c!=None:
#             x = a + b + c
#         elif a !=None and b!=None and c!= None:
#             x = a + b
#         return x
# obj = example()
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
    
    @dispatch(int, int, int, int)
    def add(self, a, b, c, d):
        x = a + b + c + d
        return x
    
obj = example()
print(obj.add(10, 20, 30))
print(obj.add(10, 20))
print(obj.add(10, 20, 30, 40))