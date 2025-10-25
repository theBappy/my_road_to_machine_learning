class myclass:
    def __init__(self):
        self.myvar=10
        return
obj = myclass()

print("class of int", type(int))
print("class of list", type(list))
print("class of dict", type(dict))
print("class of myclass", type(myclass))
print("class of obj", type(obj))