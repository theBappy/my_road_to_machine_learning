# my_set = {25, 12, 10, -21, 10, 100}
# for item in my_set:
#     print(item)

# my_set = {1, 2, 3, 4, 5}
# set_iterator = iter(my_set)

# while True:
#     try:
#         item = next(set_iterator)
#         print("Item: ", item)
#     except StopIteration:
#         break

# my_set = {1, 2, 3, 4, 5, 6, 7}
# set_iterator = iter(my_set)
# while True:
#     try:
#         item = next(set_iterator)
#         print("Item: ", item)
#     except StopIteration:
#         break

# result_set = {expression for item in iterable if condition}

# numbers = [1, 2, 3, 4, 5]
# squares_of_evens = {x ** 2 for x in numbers if x % 2 == 0}
# print(squares_of_evens)

# my_set = {1, 2, 3, 4, 5}
# set_list = list(my_set)

# for index, item in enumerate(set_list):
#     print(f"index: {index} - item: {item}")

# my_set = ()
# for i in range(5):
#     my_set.add(i)
# print(my_set)

my_set = set()
for i in range(11):
    my_set.add(i)
print(my_set)