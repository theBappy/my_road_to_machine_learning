# print(type(10))
# print(type("Hello"))
# print(type([1, 2, 3]))

# class test:
#     pass
# obj = test()
# print(type(obj))

# print(isinstance(10, int))
# print(isinstance(10, float))

# class test:
#     pass
# obj = test()
# print(isinstance(obj, test))

# class test:
#     pass
# print(isinstance(int, object))
# print(isinstance(str, object))
# print(isinstance(test, object))

# class test:
#     pass
# print(issubclass(int, object))
# print(issubclass(str, object))
# print(issubclass(test, object))

# def test():
#     pass
# print(callable("Hello"))
# print(callable(abs))
# print(callable(list.clear([1,2])))

# class test:
#     def __init__(self):
#         pass
#     def __call__(self):
#         print("Hello")
# obj = test()
# obj()
# print("Obj is callable? ", callable(obj))

# class test:
#     def __init__(self):
#         self.name = "John"
# obj = test()
# print(getattr(obj, "name"))
# setattr(obj, "age", 20)
# print(getattr(obj, "age"))
# print(hasattr(obj, "age"))

# print(dir(int))
# print(dir(dict))

class test:
    def __init__(self):
        self.name = "John"
obj = test()
print("dir(obj): ", dir(obj))
