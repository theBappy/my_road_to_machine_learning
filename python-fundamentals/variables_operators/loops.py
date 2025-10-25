# zen = '''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# '''
# for char in zen:
#     if char in "aeiou":
#         print(char, end=" ")

# numbers = (34,54,67,21,78,97,45,44,80,19, 11)
# total = 0
# for num in numbers:
#     total += num
# print(total)

# numbers = [34,54,67,21,78,97,45,44,80,19, 11]
# total = 0
# for num in numbers:
#     if num % 2 == 1:
#         print(num)

# for num in range(10):
#     print(num)

# for num in range(2, 10, 2):
#     print(num)

# for num in range(10, 20, 2):
#     print(num, end = ' ')
# print()

# for i in range(1, 10,3):
#     print(i, end =' ')
# print()
# for x in numbers:
#     print(numbers[x])
# for x in numbers:
#     print(x)

# for x in numbers:
#     print(numbers[x])

# for num in numbers:
#     # print(num)
#     print(numbers[num])
# for key in numbers.keys():
#     print(key)
# for value in numbers.values():
#     print(value)
# for key, value in numbers.items():
#     print(f"{key} - {value}")
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# for key, value in enumerate(numbers.items()):
#     print(f"{key} - {value}")

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print("%d equals %d * %d" % (num, i, j))
            break
        else:
            print(num, "is a prime number")
            break
        