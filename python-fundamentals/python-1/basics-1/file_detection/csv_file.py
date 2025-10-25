
import csv

employees = [[
    "Name", "Age", "Job"
],[
    "John", 30, "Cook"
],[
    "David", 37, "Unemployed"
],[
    "Sandy", 27, "Student"
]]

file_path = "G:\\Desktop\\new_csv.csv"

try:
    with open(file_path, 'w', newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")