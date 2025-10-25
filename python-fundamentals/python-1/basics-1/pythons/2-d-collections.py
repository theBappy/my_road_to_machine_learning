
from array import *
arr = [[1,2,3],[4,5,6],[7,8,9]]

print("Original Array")
for _ in arr:
    for i in _:
        print(i, end=" ")
    print()

arr[0][1] = -2
arr[1][1] = -3
arr[2][1] = -4
new_arr = [10, 11, 12]
arr[1] = new_arr
del(arr[0][0])
del(arr[1][0])
del(arr[2][0])
del(arr[0])
print("Modified Array: ")
for _ in arr:
    for i in _:      print(i, end=" ")
    print()

# print("Original Array: ")
# for _ in arr:
#     for i in _:
#         print(i, end=" ")
#     print()

# arr[1].insert(3, 12)
# arr[2].insert(5, 1)
# arr[0].insert(0,0)
# print("Modified array: ")
# for _ in arr:
#     for i in _:
#         print(i, end=" ")
#     print()
# print("Original array ")
# for _ in arr:
#     for i in _:
#         print(i, end=" ")
#     print()
# arr.insert(3, [11, 12, 13])
# print("Modified array ")
# for _ in arr:
#     for i in _:
#         print(i, end=" ")
#     print()

# print("Element at [1][0]: ", arr[1][0])
# print("Element at [2]: ", arr[2])

# for _ in arr:
#     for i in _:
#         print(i, end=" ")
#     print()