# import array as arr
# a = arr.array("i", [1, 2, 3])
# a.append(4)
# a.append(5)
# a.append(6)
# a.append(7)
# a.append(8)
# a.append(9)
# a.append(10)
# print(a)

import array as arr
a = arr.array("i", [1, 2, 3, 4, 5])
b = arr.array("i", [5, 6,7,8])
a.extend(b)
print(a)

# a = arr.array("i", [1, 2, 3])
# a.insert(0, 1000)
# a.insert(1, 2000)
# a.insert(2, 3000)
# a.insert(3, 4000)
# a.insert(4, 5000)
# print(a)