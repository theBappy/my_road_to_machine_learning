# nested_dict = {
#     "outer_key1": {
#         "inner_key1": "value1",
#         "inner_key2": "value2"
#     },
#     "outer_key2": {
#         "inner_key3": "value3",
#         "inner_key4": "value4",
#     }
# }
# for value in nested_dict.values():
#     print(value)
# for key in nested_dict:
#     print(key)

# nested_dict = {}
# outer_keys = ["outer_key1", "outer_key2"]
# for key in outer_keys:
#     nested_dict[key] = {"inner_key1": "value1", "inner_key2": "value2"}
# print(nested_dict)

# students = {
#     "Alice": {
#         "age": 21,
#         "major": "CSE"
#     },
#     "Bob": {
#         "age": 22,
#         "major": "EEE"
#     }
# }
# students["Alice"]["GPA"] = 3.8
# students["Charlie"] = {"age": 23, "major": "MCE"}
# print(students)
# students["Alice"]["age"] = 23
# print(students["Alice"])

students = {
    "Alice": {"age": 21, "major": "Computer Science"},
    "Bob": {"age": 20, "major": "Engineering"},
    "Charlie": {"age": 22, "major": "Mathematics"}
}

for student, details in students.items():
    print("Student: ", student)
    for key,value in details.items():
        print(f"{key} - {value}")

# for student, details in students.items():
#     print(f"Student: ", {student})
#     for key, value in details.items():
#         print(f"{key} - {value}")

# del students["Alice"]
# print(students)
# dave_major = students.get("Dave", {}).get("major", "not found")
# print(dave_major)
# bob_major = students.get("Bob", {}).get("major", "not found")
# print(bob_major)
# alice_major = students.get("Alice", {}).get("major", "Not found")
# print(alice_major)
# alice_major = students["Alice"]["major"]
# print(alice_major)
# alice_age = students["Alice"]["age"]
# print(alice_age)
# charlie_major = students["Charlie"]["major"]
# print(charlie_major)