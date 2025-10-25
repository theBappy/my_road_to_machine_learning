student_info = {
    "name":  "Alice",
    "age": 23,
    "major": "CSE",
    "graduation_year": "2021",
    "address": "london",
    "city": "UK",
    "phone": "+124-1383029"
}
# for key in student_info:
#     print(key)
# for key in student_info.keys():
#     print(key)
# for value in student_info.values():
#     print(value)

for key, value in student_info.items():
    print(f"{key} - {value}")