# import array as arr
# numerice_array = arr.array("i", [111,222,333,444,555])
# print(numerice_array[0])
# print(numerice_array[-1])
# print(numerice_array[2:])
# print(numerice_array[1])
# print(numerice_array[2])

# import array as arr
# numeric_array = arr.array("i", [1, 2, 3, 4, 5])
# for x in numeric_array:
#     print(x)

# import array as arr
# numeric_array = arr.array("i", [111, 211, 311, 411, 511])
# for location, value in enumerate(numeric_array):
#     print(f"{location} - {value}")

import array as arr
numeric_array = arr.array("i", [1, 2, 3, 4, 5, 6, 7])
print(numeric_array[:2])
print(numeric_array[2:])
print(numeric_array[:-2])
print(numeric_array[-1])
print(numeric_array[2:6])
print(numeric_array[0:4])
