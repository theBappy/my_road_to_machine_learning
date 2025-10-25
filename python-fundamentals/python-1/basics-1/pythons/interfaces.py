from abc import ABC, abstractmethod

class demoInterface(ABC):
    @abstractmethod
    def method1(self):
        print("abstract method1")
        return
    @abstractmethod
    def method2(self):
        print("abstract method2")
        return
    
class concreteclass(demoInterface):
    def method1(self):
        print("this is method1")
        return
    def method2(self):
        print("this is method2")
        return
    
obj = concreteclass()
obj.method1()
obj.method2()


class informalInterface:
    def displayMsg(self):
        pass
class newClass(informalInterface):
    def displayMsg(self):
        print("this is my message")

obj = newClass()
obj.displayMsg()