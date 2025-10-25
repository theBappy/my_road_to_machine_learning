import json

file_path = "G:\\Desktop\\output.json"

try: 
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content['name'])
        print(content['age'])
        print(content['job'])
except FileNotFoundError:
    print(f"That file was not found")
except PermissionError:
    print("You do not have permission to read that json file")