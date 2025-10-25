# file = open("example.txt", 'r')
# file = open("example.txt", 'w')
# file = open("example.txt", "a")
# file = open("example.txt", "rb")

# fo = open("foo.txt", "wb")
# print("name of the file: ", fo.name)
# print("mode of the file: ", fo.mode)
# print("closed or not: ", fo.closed)
# fo.close()

# with open("foo.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("foo.txt", "r") as file:
#     content = file.readline()
#     print(content)

# with open("foo.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()

# with open("foo.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end="")

# with open("example.txt", "w") as file:
#     file.write("Hello World")
#     print("content written successfully")

# lines = ["First line\n", "Second line\n", "Third line\n"]

# with open("example.txt", "w") as file:
#     file.writelines(lines)
#     print("content written succeeded")

# file = open("example.txt", "w")
# file.write("this is an example")
# file.close()
# print("file closed successfully")

# with open("example.txt", "w") as file:
#     file.write("another example")
#     print("file closed successfully")

try: 
    file = open("example.txt", "w")
    file.write("with try-finally")
finally:
    file.close()
    print("file closed successfully")
