student_info = {
    "name":  "Alice",
    "age": 23,
    "major": "CSE",
    "graduation_year": "2021",
    "address": "london",
    "city": "UK",
    "phone": "+124-1383029"
}
key_to_remove = ["phone", "city", "address"]
for key in key_to_remove:
    student_info.pop(key, None)
print(student_info)
# key_to_remove = ["name", "age", "major"]
# for key in key_to_remove:
#     student_info.pop(key, None)
# print(student_info)
# key_to_remove = ["name", "age"]
# for key in key_to_remove:
#     student_info.pop(key, None)
# print(student_info)

# del student_info["age"]
# print(student_info)
# student_info.pop("name")
# print(student_info)
# popped_item = student_info.popitem()
# print(student_info)
# print(popped_item)
# print(student_info.clear())
# student_info.clear()
# print(student_info)