class myclass:
    def __init__(self):
        self.myvar = 10
        return
obj = myclass()
print(type(int))
print(type(list))
print(type(dict))
print(type(myclass))
print(type(obj))

anon = type("", (object, ), {})
obj = anon()
print(type(obj))

def getA(self):
    return self.a

obj = type('',(object,),{'a':5,'b':6,'c':7,'getA':getA,'getB':lambda self : self.b})()

print(obj.getA(), obj.getB())