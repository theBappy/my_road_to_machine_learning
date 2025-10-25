# Iterable = An object/collection that can return it's element one at a time, allowing it to be iterated over in a loop

# numbers = [1, 2, 3, 4, 5]

# for number in reversed(numbers):
#     print(number, end=" - ")

# numbers = (1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)

# fruits = {"apple", "orange", "banana", "coconut"}

# for fruit in reversed(fruits):
#     print(fruit)

# name = "John Doe"
# for char in name:
#     print(char, end=" ")

my_dict = {"A": 1, "B": 2, "C": 3, "D": 4}

for key, value in my_dict.items():
    print(f"{key} : {value}")