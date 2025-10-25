# list1 =["Rohan", "Physics", 21, 69.75]
# list2=[1, 2, 3, 4 ]
# list3 =['a', 'b', 'c','d']
# list4 = [25.5, True, -55, 1+2j]

# list1 = ["physics", "chemistry", 1997, 2000]
# list2 = [1, 2, 3, 4, 5, 6, 7]
# print("list[0]: ", list1[0])
# print(list2[1 : 4])
# print(list2[-1])
# print(list2[::-1])
# print("Value available at index: ")
# print(list1[2])
# list1[2] = 2002
# print(list1)
# list2[1] = 'math'
# print(list1[1])
# list2[0] = 'physics'
# list2[1] = 'chemistry'
# list2[2] = 101
# list2[3] = 1001
# print(list2)
# print(list2[2])


# print(list2)
# del list2[0]
# print(list2)
# del list2[-1:-2]
# print(list2)
# print(list1)
# del list1[0]
# print("After deleting value at index 0: ")
# print(list1)

# list1 = ['Physics', 'Chemistry', 1997, 2002]
# list2 = [1, 2, 3,4, 5,6,7]
# print(list2)
# del list2[0:2]
# print(list2)
# lis1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(lis1 + list2)
# print([1, 2, -7] * 2)

# list1 = [1, 2, 'Physics', -2]
# print(3 in list1)
# print('Physics' in list1)
# print('Chemistry' not in list1)

# list1= ['spam', 'Spam', 'SPAM!']
# print(list1[2])
# print(list1[-2])
# print(list1[1:])
# print(list1[::-1])
# list1.append('SPAMMING')
# print(list1[-1])
# print(list1)
# list3 = [1,2,33,45,66]
# print(list3)
# list3[0]=1001
# print(list3)
# list1 = ['a', 'b','c', 'd']
# print("Original list: ", list1)
# list2 = ['Y', 'Z']
# list1[1:3] = list2
# print(list1)
# list1=['a', 'b', 'c', 'd']
# print(list1)
# list2 =['Z']
# list1[1:3] = list2
# print(list1)
# print("Original list: ", list1)
# list2 = ['X', 'Y', 'Z']
# list1[1:3] = list2
# print("List after changing  with sublist: ", list1)
# list1=['a', 'b', 'c', 'd']
# print(list1)
# list1.append('e')
# print(list1)
# list1.append('f')
# list1 = ['Rohan', 'Physics', 'Chemistry', 14, 68.89]
# print(list1)
# list1.insert(0, 'John')
# print(list1)
# print(list1.insert(1, 'Math'))
# list1 = [1, 2, 3]
# another_list = [4, 5, 6]
# list1.extend(another_list)
# print(list1)
# list1 = ['Rohan', 'Physics', 21, 69.75]
# print(list1)
# list1.remove('Rohan')
# print(list1)
# list1.remove('Physics')
# print(list1)
# list1.append('new')
# print(list1)
# list1.remove(21)
# print(list1)

# print(list2)
# list2.pop()
# print(list2)
# list2.pop()
# print(list2)

# list2 = [25.50, True, -55, 1+2j]
# print(list2)
# list2.pop()
# print(list2)
# list2.pop(0)
# print(list2)
# list2.pop(-1)
# print(list2)
# my_list = [1, 3, 5, 6]
# print(my_list.clear())
# list1 = ["a", "b", "c", "d"]
# del list1[1]
# print(list1)
# del list1[-1:-2]
# print(list1)
# list1 = [25.50, True, -55, 1+2j]
# del list1[0:3]
# print(list1)
# lst = [25, 12, 10, -21, 10, 100]
# for num in lst:
#     print(num+1)
# my_list = [1, 2, 4, 5, 7, 9]
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1
# my_list = [1, 2, 3, 4, 5]
# index = 0
# while index < len(my_list):
#     print(my_list[index])
#     index += 1

# lst = [25, 12, 10, -21, 10, 100]
# indices = range(len(lst))
# for i in indices:
#     print("lst[{}]".format(i), lst[i])
# [expression for item in iterable]
# [expression for item in iterable]
# [expression for item in iterable]
# numbers = [1, 2, 3, 4, 5, 6]
# print([num * 2 for num in numbers])
# print([num * 3 for num in numbers])
# for index , item in enumerate(iterable)

# fruits = ['apple', 'cherry', 'jackfruit']
# for idx, item in enumerate(fruits):
#     print(f"{idx}-{item}")

# [expression for item in iterable if condition]

# string = "Hello World"
# uppercase_letters = [char.upper() for char in string if char.isalpha()]
# uppercase_letters = [char.upper() for char in string if char.isalpha()]
# print(uppercase_letters)
# lowercase_letters = [char.lower() for char in string if char.isalpha()]
# print(lowercase_letters)


# original_list = [1, 2, 3, 4, 5]
# add_one = [(lambda x: x + 1)(x) for x in original_list]
# print(add_one)
# doubled_list = [(lambda x: x * 2)(x) for x in original_list]
# print(original_list)
# doubled_list = [(lambda x: x * 2)(x) for x in original_list]
# print(doubled_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined_list = [(x, y) for x in list1 for y in list2]
# print(combined_list)
# combined_list = [(x, y) for x in list1 for y in list2]
# print(combined_list)

# list1 = [x for x in range(1, 21) if x % 2 == 0]
# print(list1)
# print([x for x in range(1, 21) if x % 2 ==1])
# list1 = [num for num in range(1, 21) if num % 2 ==0]
# print(list1)
# chars = []
# for ch in 'TutorialsPoint':
#     if ch not in 'aeiou':
#         chars.append(ch)
# print(chars)
# listObj = [x for x in iterable]
# listObj = [ch for ch in 'TutorialsPoint' if ch not in 'aeiou']
# print(listObj)
# squares = [x*x for x in range(1, 21, 2)]
# print(squares)
# list1=['physics', 'chemistry', 'math', 'english']
# print(list1)
# list1.sort()
# print(list1)
# list1.sort()
# list1.sort()
# list1.sort()
# list1.sort()
# list1.sort()
# list1.sort()
# list1.sort()
# list2 = [10,16, 9, 24, 5]
# print(list2)
# list2.sort()
# print(list2)
# print(numbers)
# sorted_numbers_desc = sorted(numbers, reverse=True)
# print(sorted_numbers_desc)
# sorted_numbers_asc = sorted(numbers)
# print(sorted_numbers_asc)
# print(sorted(numbers))
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# print(sorted(numbers, reverse=True))
# list1.sort(key=str.lower)
# print(list1)
# list1.sort(key=str.lower)
# print(list1)
# list1.sort(key=str.lower)
# print(list1)
# list1 = ['Physics', 'biology', 'Biomechanics', 'psychology']
# list1.sort(key=str.upper)
# print(list1)
# def myFunction(x):
#     return x % 10
# list1=[17,23,46,51,90]
# list1.sort(key=myFunction)
# print(list1)

# import copy
# original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # creating a shallow copy
# shallow_copied_list = copy.copy(original_list)
# # modifying an element in the shallow copied list
# shallow_copied_list[0][0] = 100
# print("Original list: ", original_list)
# print("Shallow copied list: ", shallow_copied_list)

# import copy 
# original_list = [[1,2,3], [4,5,6], [7,8,9]]
# shallow_copied_list = copy.copy(original_list)
# shallow_copied_list[0][0] = 100
# shallow_copied_list[1][0] = 1000
# shallow_copied_list[2][0] = 10000
# print(original_list)
# print(shallow_copied_list)

# import copy
# original_list = [[1,2,3], [4,5,6], [7,8,9]]
# deep_copied_list = copy.deepcopy(original_list)
# deep_copied_list[0][0] = 100
# print(original_list)
# print(deep_copied_list)

# original_list = [1,2,3,4,5]
# copied_list = original_list[1:4]
# print(copied_list)
# copied_list[0] = 100
# print(copied_list)

# original_list = [1,2,3,4,5]
# copied_list = list(original_list)
# print(original_list)
# print(copied_list)


# original_list = [1,23,45]
# copied_list = list(original_list)
# print(original_list)
# print(copied_list)
# copied_list[0] = 100
# print(original_list)
# print(copied_list)

# import copy
# original_list = [1,2,3,4]
# copied_list = copy.copy(original_list)
# print(original_list)
# print(copied_list)
# copied_list[0] = 1000
# print(original_list)
# print(copied_list)
# L1 = [10,20,30,40]
# L2 = ['one', 'two', 'three', 'four']
# joined_list = L1 + L2
# print(joined_list)
# new_list =[expression for item in iterable]
# L1= [36, 24, 3]
# L2=[84,5,81]
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)
# joined_list = [item for sublist in [L1, L2] for item in sublist]

# L1 = [36, 24, 3]
# L2 = [84, 5, 81]
# joined_list =[item for sublist in [L1, L2] for item in sublist]
# joined_list =[item for sublist in [L1, L2] for item in sublist]
# joined_list = [item for sublist in [L1, L2] for item in sublist]
# print(joined_list)

# list1 = ['fruit', 'number', 'animal']
# list2 = ['apple', 5, 'dog']
# for element in list1:
#     list2.append(element)
# print(list2)

# for element in list2:
#     list1.append(element)
# print(list1)

# list1 = [10, 15, 20]
# list2 = [25, 30, 35]
# list2.extend(list1)
# print(list2)

# print(dir([]))
# print(help([].append))
# L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
# L2 = []
# for x in L1:
#     if x not in L2:
#         L2.append(x)
# print(L2)
# for x in L1:
#     if x not in L2:
#         L2.append(x)
# print(L2)

# L1=[1, 9, 1, 6, 3, 4]
# total = 0
# for num in L1:
#     total += num
# print(total)

# import random
# L1= []
# for x in range(5):
#     x = random.randint(0, 100)
#     L1.append(x)
# print(L1)

import random 
numbers = []
for num in range(5):
    num = random.randint(10,20)
    numbers.append(num)
print(numbers)