# list1 = ["physics", "biology", "chemistry", "maths"]
# print("list before sorting: ", list1)
# list1.sort()
# print("list after sorting: ", list1)
# list2 = [10, 16, 9, 24, 5]
# list2.sort()
# print(list2)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted_number_desc = sorted(numbers, reverse=False)
# print(sorted_number_desc)
# print(numbers.sort())

# list1 = ["physics", "chemistry", "biology", "psychology"]
# print("list before sorting: ", list1)
# list1.sort(key=str.lower)
# print(list1)

def myFunction(x):
    return x % 10
list1 = [17, 23, 46, 51, 90]
print("list before sorting: ", list1)
list1.sort(key=myFunction)
print('list after sorting: ', list1)