# file = open("example1.txt", "w")
# file.write("Hello, World!")
# file.close()
# print("file closed successfully")

# file = open("example.txt", "a")
# file.write("\nAnother Hello World")
# file.close()
# print("file closed successfully")

# with open("example.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a new line.\n")
# print("file closed successfully")


# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("example.txt", "w") as file:
#     file.writelines(lines)
# print("file closed successfully")

# fo = open('foo.txt', "w")
# fo.write("python is a great language.\nYeah it's great!!!\n")
# fo.close()

# with open("example.txt", "wb") as file:
#     data = b"Hello World!!!"
#     file.write(data)

# with open("example.txt", "wb") as file:
#     data = "this is txt file".encode("utf-8")
#     file.write(data)

# fo = open("example.txt", "a")
# text = "\nNew lines needs to be added at the end"
# fo.write(text)

# fo.close()

fo = open("example.txt", "w+")
fo.write("this is a rat race")
fo.seek(10, 0)
data = fo.read(3)
fo.write("\ncat")
fo.close()
