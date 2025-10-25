# marks = 80
# result = ""
# if marks < 80:
#     result = "Failed"
# elif marks > 75:
#     result = "Passed with distinction"
# else:
#     result = "Passed"
# print(result)

# def checkVowel(n):
#     match n:
#         case "a":
#             return "vowel is a"
#         case "e":
#             return "vowel is e"
#         case "i":
#             return "vowel is i"
#         case "o":
#             return "vowel is o"
#         case "u":
#             return "vowel is u"
#         case _:
#             return "no vowel"
# print(checkVowel("e"))
# print(checkVowel("u"))
# print(checkVowel('k'))

# words = ["one", "two", "three"]
# for x in words:
#     print(x)

# i = 1
# while i < 10:
#     print(i)
#     i += 1

# i = 1
# while i < 10:
#     print(i)
#     i += 2

# Jump Statement

# x = 0
# while x < 10:
#     print("x: ",x)
#     if x == 8:
#         print("Breaking....")
#         break   
#     x += 1
# print('End')

# x = 0
# while x < 10:
#     print("x: ",x)
#     if x == 7:
#         print("Breaking...")
#         break
#     x += 1
# print("End")

# for letter in "python":
#     if letter == "h":
#         continue
#     print("current letter: ",letter)

# for letter in "python":
#     if letter == 't':
#         continue
#     print("Current letter by skipping t: ", letter)

for letter in "python":
    if letter == "p":
        continue
    print("Current letter without p: ", letter)


