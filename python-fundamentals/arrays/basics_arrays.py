# import array as arr
# a = arr.array('i', [1, 2, 3])
# print(type(a), a)

# b = arr.array('u',"BAT")
# print(type(b), b)

# c = arr.array("d", [1.1, 1.2, 1.3])
# print(type(c), c)

# from array import *
# array1 = array('i', [10, 20, 30, 40, 50])
# print(array1[0])
# print(array1[::-1])
# print(array1[2:])

# from array import *
# array1 = array('i', [10, 20, 30, 40, 50])
# array1.insert(-1, 100)
# for x in array1:
#     print(x)
# array1.insert(0, 100)
# for x in array1:
#     print(x)
# array1.insert(1, 60)
# for x in array1:
#     print(x)

# from array import *
# array1 = array("i", [10, 20, 30, 40, 50])
# array1.remove(20)
# for x in array1:
#     print(x)
# array1.remove(10)
# for x in array1:
#     print(x)

# from array import *
# array1 = array('i', [10, 20, 30, 40, 50])
# print(array1.index(10))
# print(array1.index(20))
# print(array1.index(30))
# print(array1.index(40))
# print(array1.index(50))
# print(array1.index(60))


from array import *
array1 = array('i', [10, 20, 30, 40, 50])
array1[0] = 99
for x in array1:
    print(x)
# array1[1] = -99
# print(array1)
# array1[-1] = 99
# for x in array1:
#     print(x)
# array1[0] = 99
# for x in array1:
#     print(x)