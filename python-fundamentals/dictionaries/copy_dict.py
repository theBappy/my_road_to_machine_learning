# original_dict = {
#     "name": "Alice",
#     "age" : 25,
#     "skills": ["Python", "Data Science"]
# }
# shallow_copy = dict(original_dict)
# print(shallow_copy)
# shallow_copy["age"] = 56
# print(original_dict)
# print(shallow_copy)
# shallow_copy["skills"].append("DSA")
# print(original_dict)

# shallow_copy = original_dict.copy()

# print(shallow_copy)

# shallow_copy["age"] = 34
# print(original_dict)
# print(shallow_copy)

# shallow_copy["skills"].append("Machine learning")
# print(original_dict)

import copy
original_dict = {
    "name": "Alice",
    "age" : 25,
    "skills" : ["Python", "JS"],
    "education": {
        "degree": "CSE",
        "field": "AI"
    }
}
new_dict = original_dict.copy()
print(new_dict)
# deep_copy = copy.deepcopy(original_dict)
# deep_copy["age"] = 34
# deep_copy["skills"].append("Design")
# print(original_dict)
# print(deep_copy)
# print(deep_copy)
# deep_copy = copy.deepcopy(original_dict)
# print(deep_copy)