# from enum import Enum, unique

# @unique
# class Subjects(Enum):
#     ENGLISH = 1
#     MATHS = 2
#     SCIENCE = 3
#     CHEMISTRY = 2

# obj = Subjects.MATHS
# print(type(obj))

from enum import Enum
class subjects(Enum):
    english = 'e'
    maths = 'm'
    physics = 'p'
    chemistry = 'c'

for sub in subjects:
    print(sub.name, sub.value)

print(subjects("e"))
print(subjects["english"])


# obj = subjects.chemistry
# print(type(obj))
# print(obj.name)
# print(obj.value)