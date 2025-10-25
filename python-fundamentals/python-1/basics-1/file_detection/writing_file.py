# .txt, json, csv

txt_data = "I like pizza"

employees = ["Eugene", "John", "David", "Jenny"]



# file_path = "output.txt"
file_path = "G:\\Desktop\\output.txt"
try:
    with open(file_path,"a") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists.")

