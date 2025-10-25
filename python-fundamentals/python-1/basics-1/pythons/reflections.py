# print(type(10))
# print(type(2.55))
# print(type(2+3j))
# print(type("Hello World"))
# print(type([1,2,3]))
# print(type({"One":1, "Two": 2}))

# class test:
#     pass
# obj = test()
# print(type(obj))

# print(isinstance(10, int))
# print(isinstance(2.55, float))
# print(isinstance(2+3j, complex))
# print(isinstance("Hello World", str))

# print(isinstance([1,2,3], tuple))
# print(isinstance({1: 'Two', 2: 'Three'}), set)

# class test:
#     pass
# obj = test()
# print(isinstance(obj, test))

# class test:
#     pass
# print(isinstance(int, object))
# print(isinstance(str, object))
# print(isinstance(test, object))
# print(issubclass(int, object))
# print(issubclass(str, object))
# print(issubclass(test, object))

# def test():
#     pass

# print(callable("Hello"))
# print(callable(abs))
# print(callable(list.clear([1,2])))
# print(callable(test))

# class test:
#     def __init__(self):
#         pass
#     def __call__(self):
#         print("Hello")
# obj = test()
# obj()
# print("obj is callable?: ", callable(obj))

# class test:
#     def __init__(self):
#         self.name= "John"
# obj = test()
# print(getattr(obj, "name"))
# setattr(obj, "age", 20)
# setattr(obj, "name" "Jenny")
# print(obj.name, obj.age)

# class test:
#     def __init__(self):
#         self.name = "John"
# obj = test()
# print(hasattr(obj, 'age'))
# print(hasattr(obj, 'name'))

print("dir(int): ", dir(int))
print("dir(dict): ", dir(dict))

class test:
    def __init__(self):
        self.name = "Jenny"
obj = test()
print("dir(obj): ", dir(obj))