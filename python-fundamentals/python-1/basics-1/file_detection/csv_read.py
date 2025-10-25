import csv

file_path = "G:\\Desktop\\new_csv.csv"

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileExistsError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to read this csv file")