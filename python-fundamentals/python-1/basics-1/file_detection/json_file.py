
import json

employee = {
    "name": "John",
    "age": 30,
    "job": "cook"
}

file_path = "G:\\Desktop\\output.json"

try:
    with open(file_path, "w") as file:
        json.dump(employee, file, indent=4)
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")
