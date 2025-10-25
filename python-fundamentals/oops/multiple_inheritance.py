# class Father:
#     def skill1(self):
#         print("Father's skill")
# class Mother:
#     def skill2(self):
#         print("Mother's skill")

# class Child(Father, Mother):
#     pass


# c = Child()
# c.skill1()
# c.skill2()
# print(Child.mro())

class A:
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("class B")
        super().show()

class C(A):
    def show(self):
        print("class C")
        super().show()

class D(B, C):
    def show(self):
        print("class D")
        super().show()

d = D()
d.show()
