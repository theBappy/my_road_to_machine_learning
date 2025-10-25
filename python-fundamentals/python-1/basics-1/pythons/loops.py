# zen = '''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# '''

# for char in zen:
#     if char not in 'aeiou':
#         print(char, end='')

# numbers =  (34,54,67,21,78,97,45,44,80,19, 11)
# total = 0
# for num in numbers:
#     total += num
# print("Total = ", total)

# numbers = [34,54,67,21,78,97,45,44,80,19, 11]
# total = 0
# for num in numbers:
#     if num % 2== 1:
#         print(num)

# for  num in range(5):
#     print(num, end= ' ')
# for num in range(10, 20):
#     print(num, end= ' ')
# for num in range(10, 20, 3):
#     print(num, end= ' ')

# for num in range(20):
#     print(num, end = ' ')

# for  num in range(5, 20):
#     print(num, end= ' ')

# for num in range(5, 20, 5):
#     print(num, end = ' ')

# for x in numbers:
#     print(x)

# for key in numbers.keys():
#     print(key)


# for value in numbers.values():
#     print(value)

# for key, value in numbers.items():
#     print(f"{key}: {value}")
# for x in numbers:
#     # print(x, ":", numbers[x]
#     print(x, "-", numbers[x])
# numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
# for num in numbers:
#     print(num, ":", numbers[num])

# for num in range(10, 20):
#     for i in range(2, num):
#         if num % i == 0:
#             j = num / i
#             print("%d equals %d * %d" % (num, i, j))
#             break
#         else:
#             print(num, "is a prime number")
#             break

# for count in range(6):
#     print("Iteration no. {}".format(count))
# else: 
#     print("for loop over. Now in else block")
# print("End of loops")

# for count in range(10):
#     print("Iteration no. {}".format(count))
# else:
#     print("for loop is over")
# print("End of the loops")

# for i in ['T', 'P']:
#     print(i)
# else:
#     print("ForLoop-else statement successfully executed")

# for i in ['T', 'P', 'Z', 'E']:
#     print(i)
#     break
# else:
#     print("Loop-else statement successfully executed")

# def positive_or_negative():
#     for i in [5, 6, 7, 8]:
#         if i >= 0:
#             print("Positive number")
#         else:
#             print("Negative number")
#             break
#     else:
#         print("Loop-else statement")

# positive_or_negative()

# count = 0
# while count < 5:
#     count += 1
#     print("Iteration no. {}".format(count))
# print("End of while loop")

# var = '0'
# while var.isnumeric():
#     var = 'test'
#     if var.isnumeric():
#         print("Your input", var)
# print("End of while loop")

# var = 1
# while var == 1:
#     num = int(input("Enter a number: "))
#     print("You entered: ", num)
# print("Good bye!")

# count = 0
# while count < 10:
#     count += 2
#     print("Iteration no. {}".format(count))
# else:
#     print("While loop over. Now in else block")
# print("End of while loop")

# flag = 0
# while flag: print("Given flag is really true!")
# print("Good bye!")

# for letter in 'python':
#     if letter == 'h':
#         break
#     print("Current letter: ", letter)
# print("Good bye!")

# var = 10
# while var > 0:
#     print("Current variable value: ", var)
#     var -= 1
#     if var == 5:
#         break
# print("Good bye!")

# no = 33
# numbers = [11,33,55,39,55,75,37,21,23,41,13]
# for num in numbers:
#     if num == no:
#         print("Number found in the list")
#         break
# else:
#     print("Number not found in list")

# for letter in "Python":
#     if letter == "h":
#         continue
#     print("Current letter: ", letter)
# print("Good bye!")

# num = 60
# print("Prime factors for: ", num)
# d = 2
# while num > 1:
#     if num % d == 0:
#         print(d)
#         num = num / d
#         continue
#     d = d + 1

# num = 75
# print("Prime factors for: ", num)
# d = 2
# while num > 1:
#     if num % d == 0:
#         print(d)
#         num = num / d
#         continue
#     d = d + 1

# for letter in "Python":
#     if letter == "h":
#         pass
#         print("This is pass block")
#     print("Current letter: ", letter)
# print("Good bye!")

# months = ["jan", "feb", "mar"]
# days = ["sun", "mon", "tue"]

# for month in months:
#     for day in days:
#         print(month, day)
# print("Good bye!")

i = 2
while i < 25:
    j = 2
    while j <= i / j:
        if not i % j:
            break
        j = j + 1
    if j > i / j:
        print(i, " is prime")
    i = i + 1
print("Good bye!")