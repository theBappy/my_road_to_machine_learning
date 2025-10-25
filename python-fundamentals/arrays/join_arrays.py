import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
b = arr.array('i', [2,7,8,11,3,10])

a.extend(b)
print(a)

# a_list = a.tolist()
# b_list = b.tolist()
# c = a_list + b_list
# joined_list = arr.array("i", c)
# print(joined_list)


# for i in range(len(b)):
#     a.append(b[i])
# print(a)