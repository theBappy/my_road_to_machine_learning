# t1 = (1, 2)
# print(type(t1))

# tup1 = (10, 20, 30)
# x, y ,z = tup1
# print(x, y, z)

# tup1 = (10, 20, 30)
# x, y = tup1
# print(x, y)
# x, y, p, q = tup1
# print(x, y, p, q)

# tup1 = (10, 20, 30)
# a, *b = tup1
# print(a, b)
# x, *y = tup1
# print(x, y)

# tup1 = (10, 20, 30, 40, 50, 60)
# a, b, c, *d = tup1
# print(a, b, c, d)

# tup1 = (10, 20, 30, 40, 50, 60)
# x, *y, z = tup1
# print(x, y, z)

tup1 = (10, 20, 30, 40, 50, 60)
*x, y, z, a = tup1
print(x, y, z, a)