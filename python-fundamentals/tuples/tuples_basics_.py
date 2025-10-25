# tup1 = () #empty tuple
# tup1 = (50, )
# print(tup1)

# tup1 = ("physics", "chemistry", 1997, 2000)
# tup2 = (1,2,3,4,5,6,7)
# print(tup1[0])
# print(tup2[2:])
# print(tup2[::-1])

# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# tup3 = tup1 + tup2
# print(tup3)

# tup = ("physics", "chemistry", 1997, 2000)
# print(tup)
# del tup
# print(tup)

# L = ('spam', 'Spam', 'SPAM!')
# print(L[2])
# print(L[-2])
# print(L[1:])

# print("abc",-4.24e39, 18+6j, 'xyz')
# x, y = 1,2
# print(x, y)

# tuple1 = ("rohan","physics", 21, 69,75)
# tuple2 = (1,2,3,4,5)
# print(tuple1[0])
# print(tuple2[2])
# print(tuple2[-1])
# print(tuple1[2])
# print(tuple1[2:-1])
# print(tuple1[1:])

# tuple1 = ("a", "b", "c", "d")
# tuple2 = (25.50, True, -55, 1+2j)
# tuple3 = (1, 2, 3, 4, 5)
# tuple4 = ("Rohan", "Physics", 21, 69.75)

# print(tuple1[1:])
# print(tuple1[:2])
# print(tuple3[0:])
# print(tuple4[:])
# print(tuple4[::-1])

# tuple1 = ("a", "b", "c", "d")
# tuple2 = (25.50, True, -55, 1+2j)
# print(tuple1[1:3])
# print(tuple2[0:3])
# T1 = (10, 20, 30, 40)
# T2 = ('one', 'two', 'three', 'four')
# T1 = T1 + T2
# print(T1)
# T1 = (37, 14, 95, 40)
# new_elements = ("green", "red", "blue", "pink")
# part1 = T1[:2]
# part2 = T1[2:]
# updated_tuple = part1 + new_elements + part2
# print(updated_tuple)

# T1 = (10, 20, 30, 40)
# list_T1 = list(T1)
# # print(list_T1)
# updated_list = [item + 100 for item in list_T1]
# print(updated_list)
# updated_tuple = tuple(updated_list)
# print(updated_tuple)

T1 = (10, 20, 30, 40)
list_T1 = list(T1)
new_elements = [50, 60, 70]
for element in new_elements:
    list_T1.append(element)
print(list_T1)
updated_tuple = tuple(list_T1)
print(updated_tuple)
