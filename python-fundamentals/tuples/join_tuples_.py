# T1 = (10, 20, 30, 40)
# T2 = ('one', 'two', 'three', 'four')
# L1 = list(T1)
# L2 = list(T2)
# L1.extend(L2)
# print(L1)
# T1 = tuple(L1)
# print(T1)

# joined_tuple = [item for subtuple in [T1,T2] for item in subtuple]
# print(joined_tuple)
# joined_tuple = [x for subtuple in [T1, T2] for x in subtuple]
# print(joined_tuple)
# joined_tuple = [item for subtuple in [T1, T2] for item in subtuple]
# print(joined_tuple)
# joined_tuple = T1 + T2
# print(joined_tuple)
# T1 = (10, 20, 30, 40)
# T2 = ('one', 'two', 'three', 'four')
# T3 = sum((T1, T2), ())
# print(T3)

# T1 = (10, 20, 30, 40)
# T2 = ('one', 'two', 'three', 'four')
# for t in T2:
#     T1 += (t, )
# print(T1)

# print(dir((1, 2)))

# print(help((1, 2).index))
# tup1 = (25, 12, 10, -21, 10, 100)
# x = tup1.index(100)
# print(x)
# print(tup1.index(10))
# print(tup1.index(-21))
# print(tup1.index(12))
# print("Tup1: ", tup1)
# x = tup1.index(10)
# print(x)
# y = tup1.index(23)
# print(y)

# tup1 = (10, 20, 45, 10, 30, 10, 55)
# print(tup1.count(10))
# print(tup1.index(45))
# print(tup1.count(10))
# print(tup1.count(20))
# print(tup1.count(45))
# print(tup1.count(30))
# print(tup1.count(55))
# print(tup1.count(10))

tup1 = (10, 20/80, 0.25, 10/40, 30, 10, 55)
print(tup1.count(0.25))