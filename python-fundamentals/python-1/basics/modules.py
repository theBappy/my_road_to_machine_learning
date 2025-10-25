# Module = a file containing code your want to include in your program use 'import' to include a module (built-in or your own), useful to break up a large program reusable separate files

# print(help("modules"))
# print(help("math"))

# import math
# import math as m
# from math import pi
# from math import e
# import math

# a, b, c, d, e = 1, 2, 3, 4, 5
# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)

import example

result = example.pi
result = example.square(4)
result = example.cube(3)
result = example.circumference(3)
result = example.area(3)

print(result)
