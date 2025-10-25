# d1 = {"Fruit": ['mango', 'banana'], "Flower": ['rose', 'lotus']}
# d2 = {('india, USA'): 'countries', ('new delhi', "new york"):"capitals" }
# print(d1)
# print(d2)

# d1 = {["mango", 'banana']: "fruit", "flower": ["rose", "lotus"]}
# print(d1)

# d1 = {"banana": "fruit", "rose": "flower", "lotus": 'flower', "mango": "fruit"}
# d2 ={"fruit": "banana", "flower": "rose", "fruit": "mango", "flower": "lotus"}
# print(d1)
# print(d2)

# sports_player = {
#     "name": "sachin",
#     "age": 48,
#     "sport": "cricket"
# }

# print(sports_player)

# student_info = dict(name="alice", age = 21, major = "cse")
# print(student_info)

# student_info = {
#     "name": "alice",
#     "age": 21,
#     "major": "cse"
# }

# name = student_info["name"]
# print(name)
# print(student_info["age"])
# print(student_info["major"])

# student_info = {
#     "name": "alice",
#     "age": 21,
#     "major": "cse"
# }

# print(student_info["name"])
# student_info['age'] = 27
# print(student_info)
# student_info["graduation_year"]= 2023
# print(student_info)

# for key in student_info:
#     print(key)
# for value in student_info.values():
#     print(value)
# del student_info["age"]
# print(student_info)
# del student_info['name']
# print(student_info)
# student_info = {
#    "name": "Alice",
#    "age": 22,
#    "major": "Computer Science",
#    "graduation_year": 2023
# }
# for key, value in student_info.items():
#     print(f"{key}: {value}")

# dict = {"Name": "Zara", "Age": 27, "Name": "John"}
# print("dict[Name]: ", dict["Name"])
# d1 = {"a": 2, "b": 4, "c": 30}
# d2 = {"a1": 20, "b1": 40, "c1": 60}
# print(d1['b'])
# d3 = d1 | d2
# print(d3)
# print(d1 |= d2)
# capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
# print(capitals["Gujarat"])
# print(capitals["Karnataka"])
# print(capitals['Telangana'])

# capitals = {"Maharashtra":"Mumbai", "Gujarat":"Gandhinagar", "Telangana":"Hyderabad", "Karnataka":"Bengaluru"}
# print(capitals.get("Gujarat"))
# print(capitals.get("Karnataka"))
# print(d1.get("Name"))
# print(d1.get("Age"))
# print(d1.get("Dept"))
# print(d1.get("Food"))
# print(d1.get("Food", "Pizza"))
# print(student_info["major"])
# print(student_info.get("graduation_year", 2023))
# all_keys = student_info.keys()
# print(all_keys)
# name = student_info['name']
# age = student_info['age']
# print(name)
# print(age)
# student_info = {
#     "name": "Alice",
#     "age": 21,
#     "dept": "cse",
#     "major": "math"
# }
# print(student_info.values())
# all_items = student_info.items()
# print("Items: ", all_items)
# for key, value in all_items:
#     print(f"{key} - {value}")

# print(person["age"])
# person['age'] = 78
# print(person["age"])
# print(person)
# person.update({"age": 24, "city":"new york"})
# print(person)
# person.update({"name":"doe", "age": 25, "city": "washington"})
# print(person)
# if person["age"] == 23:
#     person["age"] = 24
# print(person)
# if person["city"] == "london":
#     person["city"] == 'washington'
# print(person)
# person = {
#     "name": "john",
#     "age": 23,
#     "city": "london"
# }
# person["education"] = "cse"
# print(person)
# person['profession'] = 'artist'
# print(person)
# person['id'] = 'see123'
# print(person)

# person ={"name":"alice", "age":25}
# person.setdefault("city", "london")
# print(person)
# person.setdefault("city", "usa")
# print(person)
# person.setdefault("address","street lane")
# print(person)
# person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# del person['age']
# print(person)
# del person['city']
# print(person)
# del person['name']
# print(person)
# del person['education']
# print(person)
# print(person.pop('age'))
# print(person.pop('name'))
# person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# popitem_removed = person.popitem()
# print(person)
# print(popitem_removed)
# removed_age = person.pop('age')
# print(person)
# print(removed_age)
# print(marks)
# marks['Anderson'] = 66
# print(marks)
# marks.update({"Clark": 85, "Maxwell": 88})
# print(marks)
# marks = {"John": 78,"Jenny": 86,"Toad": 88, "Frank": 91}
# marks1 = {"Saliva": 51,"John": 78, "Mosaic": 61, "Lexis": 89}
# newMarks = {**marks, **marks1}
# print(newMarks)
# new_marks = {**marks, **marks1}
# print(new_marks)
# new_marks = marks | marks1
# print(new_marks)
# marks |= marks1
# print(marks)

# marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
# marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
# marks |= marks1
# print(marks)
# student = {"name": "Alice", "age": 21}
# major = student.setdefault("major", "cse")
# print(student)

# from collections import defaultdict
# d = defaultdict(int)
# d['a'] += 1
# print(d)
# d = defaultdict(list)
# d['b'].append(1)
# print(d)
# def default_value():
#     return 'n/a'
# d=defaultdict(default_value)
# print(d['c'])
# del numbers[20]
# print(numbers)
# del numbers[10]
# print(numbers)
# del numbers[30]
# print(numbers)
# del numbers
# print(numbers)
# pop_value = numbers.pop(10)
# print(numbers)
# print(pop_value)
# popitem_value = numbers.popitem()
# print(numbers)
# print(popitem_value)
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# numbers.clear()
# print(numbers)
# student_info = {
#     "name": "alice",
#     "age": 21,
#     "major": "cse"
# }
# keys_to_remove=['age', 'major']
# for key in keys_to_remove:
#     student_info.pop(key, None)
# print(student_info)
# for key in keys_to_remove:
#     student_info.pop(key, None)
# print(student_info)

# obj = numbers.items()
# print(obj)
# print("update numbers dictionary")
# numbers.update({50: "Fifty"})
# print("view automatically updated")
# print(obj)
# obj = numbers.keys()
# print("type of obj: ", type(obj))
# print('update numbers dictionary')
# numbers.update({50:"Fifty"})
# print("view automatically updated")
# print(obj)
# numbers = {10:"Ten", 20:"Twenty", 30:"Thirty",40:"Forty"}
# obj = numbers.values()
# print("type of obj: ", type(obj))
# print(obj)
# print("update numbers dictionary")
# numbers.update({50: "Fifty"})
# print(obj)

# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)
# for key, value in student.items():
#     print(f"{key} - {value}")
# for key in student:
#     print(key)
# for item in student.items():
#     print(item)
# student = {
#     "name":"Alice",
#     "age":21,
#     "major":"CSE"
# }
# original_dict = {"name": "Alice", "age": 25, "skills": ["Python", "Data Science"]}

# shallow_copy = original_dict.copy()
# shallow_copy['age'] = 26
# shallow_copy['skills'].append("Machine Learning")
# print(original_dict)
# print(shallow_copy)
# original_dict = {"name": "Alice", "age":25, "skills": ["JS", "C++"]}
# shallow_copy = dict(original_dict)
# shallow_copy["age"] = 27
# shallow_copy["skills"].append("Python")
# print(original_dict)
# print(shallow_copy)

# import copy
# original_dict = {
#     "name": "alice",
#     "age": 25,
#     "skills": ["Python", "Data Science"],
#     "education": {
#         "degree": "Bachelor's",
#         "field": "CSE"
#     }
# }
# deep_copy = copy.deepcopy(original_dict)
# deep_copy['age'] = 35
# print(original_dict)
# print(deep_copy)

# dict1 = {"name": "Alice","age": 27,"doy": 1999}
# dict2 = dict1.copy()
# print(dict1)
# print(dict2)

# nested_dict = {
#     "outer_key1": {
#         "inner_key1": "value1",
#         "inner_key2": "value2"
#     },
#     "outer_key2": {
#         "inner_key3": "value3",
#         "inner_key4": "value4"
#     },
#     "outer_key3": {
#         "inner_key5": "value5",
#         "inner_key6": "value6"
#     }
# }
# print(nested_dict)

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
#         "age": 20,
#         "major": "Engineering"
#     }
# }
# alice_major = students["Alice"]['major']
# print(alice_major)
# bob_age = students["Bob"]['age']
# print(bob_age)
# students["Alice"]["GPA"] = 3.8
# students["Charlie"] ={"age": 22, "major":"Chemistry"}
# print(students)

# del students['Alice']
# print(students)
# alice_major = students.get("Alice", {}).get("major", "Not found")
# print(alice_major)

# dave_major = students.get("Dave", {}).get("major", "Not found")
# print(dave_major)
# students = {
#     "Alice": {"age": 21, "major": "Computer Science"},
#     "Bob": {"age": 20, "major": "Engineering"},
#     "Charlie": {"age": 22, "major": "Mathematics"}
# }
# for student, details in students.items():
#     print(f"Student: {student}")
#     for key, value in details.items():
#         print(f"{key} - {value}")

# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
# keys = ['one', 'five']
# d2 = {}
# for key in keys:
#     d2[key] = d1[key]
# print(d2)

# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
# L1 = list(d1.items())
# print(L1)

d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
vals = list(d1.values())
u_vals = [v for v in vals if vals.count(v) == 1]
d2 = {}

for k, v in d1.items():
    if v in vals:
        d = { k: v }
        d2.update(d)

print("dict with unique value: ", d2)
