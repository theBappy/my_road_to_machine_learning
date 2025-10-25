# from abc import ABC, abstractmethod
# class demoInterface(ABC):
#     @abstractmethod
#     def method1(self):
#         print("abstract method-1")
#         return
#     @abstractmethod
#     def method2(self):
#         print("abstract method-2")
#         return

# class concreteClass(demoInterface):
#     def method1(self):
#         print('this is concrete class method-1')
#         return 
#     def method2(self):
#         print('this is concrete class method-2')
#         return 
    
# obj = concreteClass()
# obj.method1()
# obj.method2()

class demoInterface:
    def displayMsg(self):
        pass
class newClass(demoInterface):
    def displayMsg(self):
        print("This is my new class message")
obj = newClass()
obj.displayMsg()