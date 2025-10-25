# import array as arr
# a = arr.array('i', [10,5,15,4,6,20,9])
# for i in range(0, len(a)):
#    for j in range(i+1, len(a)):
#       if(a[i] > a[j]):
#          temp = a[i]
#          a[i] = a[j]
#          a[j] = temp
# print (a)


# for i in range(0, len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] > a[j]:
#             temp = a[j]
#             a[i] = a[j]
#             a[j] = temp
# print(a)

# import array as arr
# original_array = arr.array("i", [10,5,15,4,6,20,9])
# print("original array: ", original_array)
# sortedList = original_array.tolist()
# sortedList.sort()
# sorted_array = arr.array("i", sortedList)
# print(sorted_array)

import array as arr
a = arr.array("i", [4, 5, 6, 8, 10, 15, 20])
# sorted(a, reverse=False)
sorted(a)
print(a)