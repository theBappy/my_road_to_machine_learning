# tup1 = ("Rohan", "Physics", 21, 69.75)
# tup2= (1,2,3,4,5)
# tup3 = ('a', 'b', 'c', 'd')
# tup4 = (25.50, True, -55, 1+2j)
# tup1 = () #empty tuple
# tup1 = (57, )
# tup1 = (34, )
# tup2 = (45, )
# tup3 = ("rohan",)
# tup4 = ("Alexia", )
# tup4 = ('one value needs comma in last',)
# tup1 = ("Physics", "Chemistry", 1997, 2002)
# tup2 = (1, 2,3,4, 5,6,7)
# print(tup1[0])
# print(tup2[1:5])
# print(tup1[::-1])
# print(tup1[0:3])

# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# tup3 = tup1 + tup2
# print(tup3)

# tup =('Physics', "chemistry", 1997, 2000)
# print(tup)
# del tup
# print(tup)
# tup1 = (1,2,3)
# tup2 = (4,5,6)
# print(tup1 + tup2)
# print(tup1*2)
# print(1 in tup1)
# print(7 in tup2)
# L = ('spam', 'Spam', 'SPAM!')
# print(L[2])
# print(L[-2])
# print(L[1:])

# print('abc', -4.24e93, 18+6.6j, 'xyz')
# x, y = 1, 2
# print("Value of x, y: ", x, y)

# tuple1 = ("Rohan", "Physics", 21, 69.75)
# tuple2 = (1, 2, 3, 4, 5)
# print(tuple1[0])
# print(tuple2[::-1])
# print(tuple1[1:3])
# print(tuple1[-1])

# tup1 = ("a", "b", "c", "d")
# tup2 = (1, 2, 3, 4, 5)
# print(tup1[1:])
# print(tup2[2:-1])

# tuple1 = ("a", "b", "c", "d")
# tuple2 = (25.50, True, -55, 1+2j)
# tuple3 = (1, 2, 3, 4, 5)
# tuple4 = ("Rohan", "Physics", 21, 69.75)
# print(tuple1[1:])
# print(tuple2[:2])
# print(tuple3[:])
# print(tuple3[:])
# print(tuple2[:])

# tuple1 = ("a", "b", "c", "d", "e")
# tuple2 = (25.50, True, -55, 1+2j)
# print(tuple1[1:3])
# print(tuple2[0:2])
# t1 = (10, 20, 30, 40)
# t2 = ("one", "two","three", "four")
# print(t1 + t2)
# t1 = (37, 14, 95, 40)
# new_elements = ('green', 'red', 'blue', 'pink')
# part1 = t1[:2]
# part2 = t1[2:]
# updated_tuple = part1 + new_elements + part2
# print(updated_tuple)
# t1 = (10, 20, 30, 40)
# list_t1 = list(t1)
# updated_list = [item + 100 for item in list_t1]
# updated_tuple = tuple(updated_list)
# print(updated_tuple)

# t1 = (10, 20, 30, 40)
# list_t1 = list(t1)
# updated_list = [num + 100 for num in list_t1]
# updated_tuple = tuple(updated_list)
# print(updated_tuple)

# t1 = (10, 20, 30, 40)
# list_t1 = list(t1)
# new_elements = [50, 60, 70]
# for element in new_elements:
#     list_t1.append(element)
# updated_tuple = tuple(list_t1)
# print(updated_tuple)

# UNPACKING TUPLE ITEMS
# tup1 = (10, 20, 30)
# x, y, z = tup1
# print("x ", x, "y: ", y, "z: ", z)
# tup1 = (10, 20, 30)
# x, y = tup1
# x, y, z, q = tup1

# tup1 = (10, 20, 30, 40)
# x, *y = tup1
# print("x: ", x, "y: ", y)

# tup1 = (10, 20, 30, 40)
# *x , y = tup1
# print("x: ", x, "y: ", y)
# tup1 = (10, 20, 30,40,50, 60)
# x, *y, z = tup1
# *x, y, z = tup1
# print("x: ", x)
# tup = (25, 12, 10, -21, 10, 100)
# for num in tup:
#     print(num, end=' ')

# my_tup = (1, 2, 3, 4, 5)
# idx = 0
# while idx < len(my_tup):
#     print(my_tup[idx])
#     idx += 1
# tup = (25, 12, 10, -21, 10, 100)
# indices = range(len(tup))
# for num in indices:
#     print("tup[{}]: ".format(num), tup[num])
# t1 = (10,20,30,40)
# t2 = ('one','two','three','four')
# joined_tuple = t1 + t2
# print(joined_tuple)
# [expression for item in iterable]
# T1 = (36, 24, 3)
# T2 = (84, 5, 81)
# joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
# print(joined_tuple)
# T1 = (10,20,30,40)
# T2 = ('one','two','three','four')
# L1 = list(T1)
# L2 = list(T2)
# L1.extend(L2)
# T1 = tuple(L1)
# print(T1)
# T1 = (10,20,30,40)
# T2 = ('one', 'two', 'three', 'four')
# joined_tuple = ((T1, T2), ())
# print(joined_tuple)
# T1 = (10,20,30,40)
# T2=('one','two','three','four')
# for t in T1:
#     T2 += (t, )
# print(T2)
# for t in T2:
#     T1 += (t, )
# print(T1)
# for t in T2:
#     T1 += (t,)
# print(T1)

# print(dir((1,2)))
# print(help((1,2).index))

# tup1 = (25,12, 10, -21, 10, 100)
# print(tup1)
# x = tup1.index(10)
# print(x)
# x = tup1.index(-21)
# print(x)
# y = tup1.index(100)
# print(y)
# z = tup1.index(10000)
# print(z)
# tup1 = (10, 20, 45, 10, 30, 10, 55)
# print(tup1.count(10))
# print(tup1.count(20))
# print(tup1.count(10))
# print(tup1.count(45))
# print(tup1.count(30))
# print(tup1.count(55))
# print(tup1.count(444))
# tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
# print(tup1)
# c = tup1.count(0.25)
# print(c)
# T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
# T2 = ()
# for x in T1:
#     if x not in T2:
#         T2 += (x, )
# print(T1)
# print(T2)
# T1 = (1, 9, 1, 6, 3, 4)
# total = 0
# for num in T1:
#     total += num
# print(sum(T1))

# import random
# t1 = ()
# for i in range(5):
#     x = random.randint(10,20)
#     t1 += (x, )
# print(t1)
