
# language = set()
# language.add("c++")
# language.add("js")
# language.add("python")
# language.add("rust")
# language.add("php")
# print(language)

# my_set = {1, 2, 3}
# my_set.update([4])
# print(my_set)
# my_set.update([5])
# print(my_set)
# my_set.update([6])
# print(my_set)
# my_set.update([7])
# print(my_set)
# my_set.update([8])
# print(my_set)

# lang1 = {"c++", "c", "js", "python"}
# lang2 = {"rust", "go", "php"}
# lang1.update(lang2)
# print(lang1)

# set1 = set("Hello")
# print(set1)
# set2 = set("World")
# set1.update(set2)
# print(set1)

# lang1 = {"js", "python", "java"}
# lang2 = {"php", "rust", "go"}
# lang3 = {"sql", "c#"}

# combined_set1 = lang1.union(lang2)
# combined_set2 = combined_set1.union(lang3)

# print(combined_set1)
# print(combined_set2)

# lang1 = {"C", "C++", "Java", "Python"}
# lang2 = ["PHP", "C#", "Perl"]

# lang3 = lang1.union(lang2)
# print(lang3)

numbers = [1,2,3,4,5]
squares_set = {num ** 2 for num in numbers}
print(squares_set)