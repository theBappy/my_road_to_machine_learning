import array as arr
import copy
a = arr.array("i", [110, 220, 330, 440, 550])
b = copy.deepcopy(a)
print(b)

print(id(a))
print(id(b))

a[1] = 1
print(a, b)

# a = arr.array("i", [110, 220, 330, 440, 550])
# b = a
# print("copied array: ", b)
# a[0] = 660
# print(a, b)
# print(id(a))
# print(id(b))