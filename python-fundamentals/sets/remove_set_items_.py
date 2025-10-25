# my_set = {"rohan", "physics", 21, 69.75}
# my_set.discard("rohan")
# print(my_set)
# my_set.discard("physics")
# print(my_set)
# my_set.discard(21)
# print(my_set)
# my_set.discard(45)
# print(my_set)
# print(my_set)
# my_set.remove("rohan")
# print(my_set)
# my_set.remove(21)
# print(my_set)
# my_set.remove("physics")
# print(my_set)
# my_set.remove("chemistry")
# print(my_set)

# my_set = {1, 2, 3, 4, 5}
# removed_element = my_set.pop()
# print(removed_element)
# print(removed_element)

# my_set = set()
# removed_element = my_set.pop()
# print(removed_element)

# my_set ={1,2,3,4,5}
# my_set.clear()
# print(my_set)


# print(s1 - s2)
# s1.difference_update(s2)
# print(s1)


# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print("s1 before running difference_update: ", s1)
# s1.difference_update(s2)
# print(s1)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# resulted_set = set1 ^ set2
# print(resulted_set)
# resulted_set = set1.symmetric_difference(set2)
# print(resulted_set)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set1.intersection_update(set2)
# print(set1)
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# result = s1.intersection_update(s2)
# print(s1)
# result = s1 & s2
# print(result)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# resulted_set = s1.intersection(s2)
# print(resulted_set)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.symmetric_difference_update(s2)
# s2.symmetric_difference_update(s1)
# print(s2)
# print(s1)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# s1.symmetric_difference(s2)
# print(s1)
s2.symmetric_difference(s1)
print(s2)