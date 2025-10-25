# class Student:
#     def __init__(self):
#         self.name = "John"
#         self.subs = self.subjects()
#         return
#     def show(self):
#         print("Name: ", self.name)
#         self.subs.display()

#     class subjects:
#         def __init__(self):
#             self.sub1 = "Phy"
#             self.sub2 = "Che"
#             return
#         def display(self):
#             print("Subjects: ", self.sub1, self.sub2)

# s1 = Student()
# s1.show()

# class Organization:
#     def __init__(self):
#         self.inner1 = self.Department1()
#         self.inner2 = self.Department2()

#     def showName(self):
#         print("Organization Name: Tutorials point")

#     class Department1:
#         def displayDepartment1(self):
#             print("In dept 1")
    
#     class Department2:
#         def displayDepartment2(self):
#             print("In dept 2")

# outer = Organization()
# outer.showName()

# inner1 = outer.inner1
# inner1.displayDepartment1()

# inner2 = outer.inner2
# inner2.displayDepartment2()


class Organization:
    def __init__(self):
        self.inner = self.Department()

    def showName(self):
        print("Organization Name: Tutorials Point")

    class Department:
        def __init__(self):
            self.innerTeam = self.Team1()
        def displayDep(self):
            print("In Department")
        class Team1:
            def displayTeam(self):
                print("Team 1 of the department")

outer = Organization()
outer.showName()

inner = outer.inner
inner.displayDep()

innerTeam = inner.innerTeam
innerTeam.displayTeam()