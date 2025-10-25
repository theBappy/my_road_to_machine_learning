class Student:
    class_year = 2023
    num_of_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_of_students += 1

student1 = Student("John", 23)
student2 = Student("Jenny", 25)
print(student1.name)
print(Student.num_of_students)
print(Student.class_year)

print(f"My graduation class of {Student.class_year} has {Student.num_of_students}")
        