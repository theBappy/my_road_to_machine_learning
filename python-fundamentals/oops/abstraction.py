from abc import ABC, abstractmethod
class demo(ABC):

    @abstractmethod
    def method1(self):
        print("abstract method")
        return
    
    def method2(self):
        print("concrete method")
        return

class concrete(demo):
    def method1(self):
        super().method1()
        return
    
obj = concrete()
obj.method1()
obj.method2()



        