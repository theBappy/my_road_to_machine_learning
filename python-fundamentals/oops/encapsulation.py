# class Student:
#     def __init__(self, name="John", age=31):
#         self.name = name
#         self.age = age
# s1 = Student()
# s2 = Student("Jenny", 33)
# print(f"Student-1: {s1.name} whose age is {s1.age}")
# print(f"Student-2: {s2.name} whose age is {s2.age}")


class Student:

   def __init__(self, name="Rajaram", marks=50):
      self.__name = name
      self.__marks = marks
   def studentdata(self):
      print ("Name: {} marks: {}".format(self.__name, self.__marks))
      
s1 = Student()
s2 = Student("Bharat", 25)

# s1.studentdata()
# s2.studentdata()

# print(f"Name: {s1.__name} Age: {s1.__marks}")
print(f"Name: {s1._Student__name} Marks: {s1._Student__marks}")
print(f"Name: {s2._Student__name} Marks: {s2._Student__marks}")