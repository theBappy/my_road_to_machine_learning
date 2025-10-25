# class SingleTon:
#     __uniqueInstance = None
#     @staticmethod
#     def createInstance():
#         if SingleTon.__uniqueInstance == None:
#             SingleTon()
#         return SingleTon.__uniqueInstance
#     def __init__(self):
#         if SingleTon.__uniqueInstance != None:
#             raise exec("Object exists!")
#         else:
#             SingleTon.__uniqueInstance = self
# obj1 = SingleTon.createInstance()
# print(obj1)
# obj2 = SingleTon.createInstance()
# print(obj2)

class SingletonClass:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            print("Creating the object")
            cls._instance = super(SingletonClass, cls).__new__(cls)
        return cls._instance

obj1 = SingletonClass()
print(obj1)
obj2 = SingletonClass()
print(obj2)