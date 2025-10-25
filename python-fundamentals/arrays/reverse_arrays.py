import array as arr
numeric_array = arr.array("i", [88, 99, 77,55, 66])
b = arr.array("i")
for i in range(len(numeric_array) - 1, -1, -1):
    print(numeric_array[i])
    b.append(numeric_array[i])

print(numeric_array)
print(b)

# b = arr.array("i")
# for i in range(len(numeric_array)-1, -1, -1):
#     b.append(numeric_array[i])
# print(numeric_array)
# print(b)



# print("array before reversing: ", numeric_array)
# newArray = list(reversed(numeric_array))
# rev_array = arr.array("i", newArray)
# print(rev_array)

# new_array = numeric_array.tolist()
# new_array.reverse()
# rev_array = arr.array('i', new_array)
# print(rev_array)

# new_array = numeric_array.tolist()
# new_array.reverse()
# revArray = arr.array("i", new_array)
# print(revArray)

# new_array = numeric_array.tolist()
# new_array.reverse()
# print(numeric_array)


# new_array = numeric_array.tolist()
# new_array = numeric_array.tolist()
# new_array = numeric_array.tolist()
# new_array = numeric_array.tolist()
# new_array = numeric_array.tolist()
# new_array = numeric_array.tolist()


# print(numeric_array)
# # print(numeric_array[::-1])
# reverse_array = numeric_array[::-1]
# print(reverse_array)