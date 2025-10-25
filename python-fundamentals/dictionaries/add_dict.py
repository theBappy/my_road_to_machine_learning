# student_info = {
#     "name":  "Alice",
#     "age": 23,
#     "major": "CSE",
#     "graduation_year": "2021",
#     "address": "london",
#     "city": "UK",
#     "phone": "+124-1383029"
# }

# student_info.update({
#     "hobby": "hunting",
#     "sport" : "badminton",
#     "job" : "SDE"
# })
# print(student_info)
# student_info["sport"] = "cricket"
# student_info["hobby"] = "hunting"
# student_info["profession"] = "SDE"
# student_info["gf"] = "Jenny"
# print(student_info)
# print(student_info)


# marks1 = {
#     "john": 61,
#     "jenny": 88,
#     "david": 56
# }
# marks2 = {
#     "moon": 45,
#     "pinkman": 23,
#     "daisy": 82
# }
# new_marks = {
#     **marks1,
#     **marks2
# }
# print(new_marks)
# student_info = {
#     "name":  "Alice",
#     "age": 23,
#     "major": "CSE",
#     "graduation_year": "2021",
#     "address": "london",
#     "city": "UK",
#     "phone": "+124-1383029"
# }
# marks ={
#     "physics": 76,
#     "maths": 67,
#     "english": 78,
#     "city": "UK"
# }
# full_info = student_info | marks
# print(full_info)

# marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
# marks2 = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
# marks1 |= marks2
# print(marks1)

# student_info = {
#     "name" : "Alice",
#     "age" : 21
# }
# major = student_info.setdefault("major", "CSE")
# print(student_info)

# from  collections import defaultdict
# d = defaultdict(int)
# d["a"] += 1
# print(d)

# from collections import defaultdict
# d = defaultdict(int)
# d["a"] += 1
# print(d)

# from collections import defaultdict
# d = defaultdict(list)
# d["b"].append(1)
# print(d)

# from collections import defaultdict
# d = defaultdict(list)
# d["a"].append(1)
# print(d)
# d["b"].append('alice')
# print(d)
# from collections import defaultdict
# def default_value():
#     return "N/A"
# d = defaultdict(default_value)
# print(d["c"])



