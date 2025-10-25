
file_path = "G:/Desktop/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("That file doesn't exist")
except PermissionError:
    print("You do not have permission to read that file")

