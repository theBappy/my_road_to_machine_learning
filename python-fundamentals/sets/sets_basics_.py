# my_set = {1, 2, 3, 4, 5}
# print(my_set)

# my_set = set([1, 2, 3, 4, 5])
# print(my_set)

# my_set = set([1, 2, 2, 3, 4, 4, 5, 5, 5])
# print(my_set)

# mixed_set = {1, "Hello", (1, 2, 3)}
# print(mixed_set)

# my_set = {1, 2, 3, 4}
# my_set.add(4)
# print(my_set)
# my_set.add(5)
# print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.add(7)
# print(my_set)

# my_set = {1, 2, 3, 4}
# my_set.remove(2)
# print(my_set)
# my_set.remove(4)
# print(my_set)
# my_set.remove(1)
# print(my_set)

my_set = {1,2,3,4}
# my_set.remove(5)
# print(my_set)
# my_set.discard(5)
# print(my_set)
# my_set.discard(4)
# print(my_set)
# my_set.discard(3)
# print(my_set)
# my_set.discard(1)
# print(my_set)

# my_set = {1,2,3,4}
# if 2 in my_set:
#     print(True)
# else:
#     print(False)

# squared_set = {num**2 for num in range(1,6)}
# print(squared_set)

# squared_set = {x ** 2 for x in range(1, 6)}
# print(squared_set)

# squared_set = {x ** 2 for x in range(1, 6)}
# print(squared_set)

# squared_set = {x ** 2 for x in range(1, 5)}
# print(squared_set)

# even_numbers = {x for x in range(1, 11) if x % 2 == 0}
# print(even_numbers)

# odd_numbers = {x for x in range(1, 11) if x % 2 == 1}
# print(odd_numbers)

# nested_set = {(x, y) for x in range(1, 9) for y in range(1, 3)}
# print(nested_set)

# nested_set = {(x, y) for x in range(1, 3) for y in range(1, 3)}
# print(nested_set)

my_frozen_set = frozenset([1, 2, 3])
print(my_frozen_set)
my_frozen_set.add(5) #raise attribute-error