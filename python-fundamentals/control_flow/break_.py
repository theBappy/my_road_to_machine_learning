# for letter in "python":
#     if letter == "h":
#         break
#     print("current letter is: ", letter)
# print("end of loop")

# var = 10
# while var > 0:
#     print("Current variable value: ", var)
#     var -= 1
#     if var == 5:
#         break
# print("end of while loop")

no = 33
numbers = [11,33,55,39,55,75,37,21,23,41,13]
for num in numbers:
    if num == no:
        print("number is found")
        break
else:
    print("number not in the list")
