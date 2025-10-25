# my_set = {1,2,3,4,5}
# print(my_set)

# my_set = set([1,2,3,4,5])
# print(my_set)
# my_set = {1,2,2,3,4,5,5,6}
# print(my_set)

# mixed_set = {1, 'hello', (1,2,3)}
# print(mixed_set)

# my_set = {1,2,3,3}
# my_set.add(4)
# print(my_set)
# my_set.add(5)
# print(my_set)
# my_set.add(6)
# print(my_set)
# my_set.add(7)
# print(my_set)

# my_set ={1,2,3,4}
# my_set.discard(4)
# print(my_set)
# my_set.discard(2)
# print(my_set)
# my_set.discard(10)
# print(my_set)
# my_set.remove(4)
# print(my_set)
# my_set.remove(1)
# print(my_set)
# my_set.remove(10)
# print(my_set)

# my_set = {1,2,3,4}
# print(1 in my_set)
# print(7 in my_set)
# print(10 not in my_set)

# set_variable = {expression for item in iterable if condition}
# {expression for item in iterable if condition}

# squared_set = {x**2 for x in range(1,6)}
# print(squared_set)
# print({x**2 for x in range(1,6)})
# print({num for num in range(1, 11) if num % 2 == 0})

# nested_set = {(x, y) for x in range(1, 3) for y in range(1,3)}
# print(nested_set)

# nested_set = {(x, y) for x in range(1, 2) for y in range(1, 4)}
# print(nested_set)

# Frozen Set
# Immutable, cannot be modified after creation
# my_frozen_set = frozenset([1, 2, 3])
# print(my_frozen_set)

# langs = {"C","C++","Java","Python"}
# for lang in langs:
#     print(lang)

# my_set ={1,2,3,4,5}
# accessed_items = [item for item in my_set]
# print(accessed_items)
# print([i for i in my_set])
# print([i for i in my_set])
# print([item for item in my_set])

# import itertools
# original_set = {1,2,3,4}
# is_subset = {1,2}.issubset(original_set)
# print(is_subset)

# my_set ={1,2,3,4,5}
# is_subset = {1,2}.issubset(my_set)
# print("{1, 2} is a subset of my_set: ", is_subset)

# subsets_with_two_elements = [set(subset) for subset in itertools.combinations(my_set, 2)]
# print(subsets_with_two_elements)
# import itertools 
# my_set = {1,2,3,45}
# subsets_with_two_elements = [set(subset) for subset in  itertools.combinations(my_set,2)]
# print(subsets_with_two_elements)

# print([set(subset) for subset in itertools.combinations(my_set, 3)])

# langs = {"C", "C++", "Python", "Java", "JavaScript"}
# if "Java" in langs:
#     print("Yes")
# else:
#     print("no")

# print("Yes" if "sql" in langs else "No")

# language = set()

# language.add("C")
# language.add("Python")
# language.add("JavaScript")
# language.add("Ruby")
# language.add("C++")
# print("Updated set: ", language)


# my_set= {1,2,3}
# my_set.update([4,5])
# print(my_set)
# my_set.update([4])
# my_set.update([5,6])
# my_set.update([""])
# print(my_set)

# lang1 ={"c", "c++", "java"}
# lang2 = {"ruby", "rust", "go"}
# lang1.update(lang2)
# print(lang1)
# lang2.update(lang1)
# print(lang2)

# set1 = set("hello")
# set2 = set("world")
# set1.update(set2)
# print(set1)
# print(set2.update("is destroyed"))

# set1= set("Hello")
# set1.update("World")
# print(set1)

# lang1 = {"c", "c++", "ruby", "python"}
# lang2 = {"php", "c#", "python"}
# lang3 = {"javascript", "c#"}
# combined_set = lang1.union(lang2)
# print(combined_set)
# combined_set2 = lang2.union(lang3)
# print(combined_set2)

# lang1 = {"C", "C++", "Java", "Python"}
# lang2 = ["PHP", "C#", "Perl"]
# lang3 = lang1.union(lang2)
# print(lang3)
# print([num ** 2 for num in numbers])
# print({num ** 2 for num in numbers})
# numbers = [1,2,3,4,5]
# print({num ** 2 for num in numbers})

# print("Original set: ", my_set)
# my_set.remove("Chemistry")
# print(my_set)
# my_set ={"John", "Chemistry", 21, 98.75}
# print("Original set: ", my_set)
# my_set.remove("John")
# print(my_set)
# lang1 = {"C", "C++", "Java", "Python"}
# print("Original set: ", lang1)
# lang1.remove("Java")
# print(lang1)
# lang1.remove("JavaScript")
# print(lang1)
# lang1.discard("C")
# print(lang1)
# lang1.discard("C++")
# print(lang1)
# lang1.discard("JavaScript")
# print(lang1)

# my_set = {1,2,3,4,5}

# removed_element = my_set.pop()
# print(removed_element)
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# print(my_set.pop())
# my_set = set()
# print(my_set.pop())
# my_set = {1,2,3,4,5,5}
# # print(my_set.clear())
# my_set.clear()
# print("Updated set: ", my_set)

# print(s2)
# s2.difference_update(s1)
# print(s2)
# print(s2.difference_update(s1))
# print("s1 before running difference update: ", s1)
# s1.difference_update(s2)
# print(s1)

# s1 = {1,2,3,4,5}
# s2 = {6,7,8,9,10,4,5,3}
# print("s1 before running difference update: ", s1)
# s1.difference_update(s2)
# print(s1)
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
# print(set1 ^ set2)
# print(set1 ^ set2)
# print(set1 ^ set2)
# print(set1 ^ set2)
# print(set1 ^ set2)
# print(set1 ^ set2)
# result_set = set1.symmetric_difference(set2)
# print(result_set)
# print(set2 ^ set1)
# set1 ={1,2,3,4}
# set2 = {3,4,5,6}
# set1.intersection_update(set2)
# print(set1)
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print(s1)
# s3 = s1.intersection(s2)
# print(s3)
# s4 = s1.intersection(s3)
# print(s4)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s1.symmetric_difference_update(s2)
# print(s1)

# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# print("s1: ", s1, "s2: ", s2)
# s3 = s1.symmetric_difference(s2)
# print("s1 ^ s2: ", s3)

# my_set = {25, 12, 10, -21, 10, 100}
# for x in my_set:
#     print(x)

# my_set = {1,2,3,4,5}
# set_iterator= iter(my_set)
# # print(set_iterator)
# while True:
#     try:
#         item = next(set_iterator)
#         print("Item: ", item)
#     except StopIteration:
#         break

# my_set = {1,2,3,4,5}
# set_iterator = iter(my_set)

# while True:
#     try:
#         item = next(set_iterator)
#         print("Item: ", item)
#     except StopIteration:
#         break

# {expression for item in iterable if condition}
# my_set = [1,2,3,4,5]
# print({num ** 2 for num in my_set if num % 2 == 0})

# set_list = list(my_set)
# for index , item in enumerate(set_list):
#     print(f"{index}: {item}")
# my_set = {1,2,3,4,5}
# set_list = list(my_set)
# for index, item in enumerate(set_list):
#     print(f"Index: {index} - Item: {item}")
# my_set = set()
# for i in range(5):
#     my_set.add(i)
# print(my_set)
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}
# s3 = s1 | s2
# print(s3)
# s3.union({7,8,91})
# print(s3)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# s3 = s1.union(s2)
# print(s3)

# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# s1.update(s2)
# print(s1)

# s1 ={1,2,3,4,5}
# s2 ={4,5,6,7,8}
# s3 = {*s1, *s2}
# print(s3)
# s1={1,2,3}
# s2 ={3,4,5}
# # joined_set = {x for s in [s1, s2] for x in s}
# # print(joined_set)
# joined_set = {x for s in [s1, s2] for x in s}
# joined_set = {x for x in [s1, s2] for x in s}
# joined_set = {x for x in [s1, s2] for x in s}
# joined_set= {x for s in [s1,s2] for x in s}

# set1 = {1,2,3}
# set2 = {3,4,5}
# joined_st = set()
# for element in set1:
#     joined_st.add(element)
# for element in set2:
#     joined_st.add(element)
# print(joined_st)

# set.copy()
# set.copy()
# set.copy()
# set.copy()
# set.copy()
# lang1={"C", "C++", "Java", "Python"}
# print("Lang1: ", lang1, "id(Lang1): ", id(lang1))
# lang2 = lang1.copy()
# print("Lang2: ", lang2, "id(Lang2): ",id(lang2))
# lang1.add("PhP")
# print("After updating lang1")
# print(lang1, id(lang1))
# print(lang2, id(lang2))

# original_set = {1,2,3,4}
# copied_set = set(original_set)
# print("Copied_set: ", copied_set)
# print(id(original_set), id(copied_set))
# copied_set.add(5)
# print("copied set: ", copied_set)
# print("original set: ", original_set)

# original_set = {1,2,3,4,5}
# print({x for x in original_set})

# set1={1,2,3}
# set2 = {3,4,5}
# set3={6,8,9}
# set4={9,45,73}
# union_set1 = set1.union(set2)
# print(union_set1)
# set5 = set3 | set4
# print(set5)

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = {6, 8, 9}
# set4 = {9, 8, 73}
# difference_set1= set1.difference(set2)
# print(difference_set1)
# difference_set2 = set3 - set4
# print(difference_set2)
# intersection_set1 = set1.intersection(set2)
# print(intersection_set1)
# intersection_set2 = set3 & set4
# print(intersection_set2)

# set1 = {1, 2, 3}
# set2 = {1,2,3,4}
# set3 = {6, 8, 9}
# set4 = {9, 8, 73}
# is_subset1 = set1.issubset(set2)
# print(is_subset1)
# is_subset2 = set3 <= set4
# print(is_subset2)
# set5 = set1.symmetric_difference(set2)
# print(set5)
# set6 = set3 ^ set4
# print(set6)

# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,8]
# s1 = set(l1)
# s2 = set(l2)
# commons = s1 & s2
# commonList = list(commons)
# print(commonList)

# s1 = {1,2,3,4,5}
# s2 = {4,5}
# if s2.issubset(s1):
#     print("true")
# else: 
#     print("false")
# T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
# s1 = set(T1)
# print(s1)