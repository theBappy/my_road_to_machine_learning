# lang1 = {"C", "C++", "Java", "Python"}
# print("lang1: ", lang1, "id(lang1): ", id(lang1))
# lang2 = lang1.copy()
# print("lang2: ",lang2, "id(lang2): ", id(lang2))

# lang1.add("php")
# print("after updating lang1")
# print("lang1: ", lang1, "id(lang1): ", id(lang1))
# print("lang2: ", lang2, "id(lang1): ", id(lang2))

# original_set = {1, 2, 3, 4}
# copied_set = set(original_set)
# print(copied_set)

# copied_set.add(5)
# print(original_set)
# print(copied_set)

original_set = {1, 2, 3, 4, 5}
copied_set = {x for x in original_set}
print(copied_set)
