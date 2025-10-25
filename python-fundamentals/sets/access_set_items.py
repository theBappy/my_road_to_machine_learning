# langs = {"js", "python", "java", "c++"}
# for lang in langs:
#     print(lang)

# my_set = {1,2,3,4,5}
# accessed_items = [item for item in my_set]
# print(accessed_items)

# import itertools

# original_set = {1, 2, 3,4}
# is_subset = {1, 2}.issubset(original_set)
# print(is_subset)

# subsets_with_two_elements = [set(subset) for subset in itertools.combinations(original_set, 2)]
# print(subsets_with_two_elements)

langs = {"c++", "python", "js", "java", "rust"}

if "java" in langs:
    print("java is present in the set")
else:
    print("java is not present in the set")

if "sql" not in langs:
    print(True)
else:
    print(False)