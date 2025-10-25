# from collections import namedtuple
# Point = namedtuple('typename', fieldnames)
# from collections import namedtuple
# Vertex = namedtuple('Vertex', ['x', 'y'])
# v = Vertex(10, 20)

# print("Vertex-1: ", v.x)
# print("Vertex-2: ", v.y)

# from collections import namedtuple
# Point = namedtuple('Point', ['x','y'])
# p = Point(10, 20)
# print("Point-1: ", p[0])
# print("Point-2: ", p[1])

# from collections import namedtuple
# Point = namedtuple("Point", ['x','y'])
# p= Point(10, 20)
# print("Point-1: ", p.x)
# print("Point-2: ", p.y)


# from collections import namedtuple
# Point = namedtuple("Point", ['x','y'])
# p = Point(10, 20)
# print("getattr(p, x): ", getattr(p,'x'))
# print("getattr(p, y): ", getattr(p, 'y'))

# from collections import namedtuple

# Point = namedtuple("Point", ['x', 'y'])
# p = Point(10, 20)
# print("Fields of p: ", p._fields)

# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)
# p2 = p._replace(x = 30)
# print("p2.x: ", p2.x)
# print("p2.y: ", p2.y)

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)
# d = p._asdict()
# print(d)
# d = p._asdict()
# print(d)

# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(10, 20)
# p2 = Point._make([30, 40])
# print("p2.x: ", p2.x)
# print("p2.y: ", p2.y)

import collections

Student = collections.namedtuple("Student",['name', 'age', 'DOB'])

S = Student('John', '14', '2541997')
li = ['Jenny', '19', '411997']
di = {'name': 'ravi', 'age': 24, 'DOB': '1391997'

print(Student(**di))}
