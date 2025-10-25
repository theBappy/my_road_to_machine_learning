# from enum import Enum, unique

# @unique
# class subjects(Enum):
#     ENGLISH = 1
#     MATHS = 2
#     PHYSICS = 3
#     CHEMISTRY = 4
# obj = subjects.MATHS
# print(type(obj))
# subjects = Enum("subjects", "ENGLISH MATHS PHYSICS CHEMISTRY")
# print(subjects.ENGLISH)
# print(subjects.MATHS)
# print(subjects.CHEMISTRY)
# print(subjects.PHYSICS)

from enum import Enum
class subjects(Enum):
    ENGLISH = "E"
    SCIENCE = "S"
    BIOLOGY = "B"
    MATHS = "M"

for sub in subjects:
    print(sub.name, sub.value)


# obj = subjects.BIOLOGY
# print(type(obj))
# print(obj.name)
# print(obj.value)