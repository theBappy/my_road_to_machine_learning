# s1 = {1, 2, 3, 4, 5}
# s2 = {4, 5, 6, 7, 8}
# s1.update(s2)
# print(s1)
# s3 = s1.union(s2)
# print(s3)
# s3 = s1 | s2
# print(s3)

# s1 = {1, 2, 3,4 ,5}
# s2 = {4, 5,6,7,8}
# s3 = {*s1, *s2}
# print(s3)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# s3 = {*s2, *s1}
# print(s3)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# s3 = {*s1, *s2}
# print(s3)
# joined_set = {item for multiItem in [set1 , set2] for item in multiItem}
# print(joined_set)
# joined_set = {x for s in [set1, set2] for x in s}
# print(joined_set)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# joined_set = {x for s in [set1, set2] for x in s}
# print(joined_set)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
joined_set = set()
for element in set1:
    joined_set.add(element)
for element in set2:
    joined_set.add(element)
print(joined_set)
