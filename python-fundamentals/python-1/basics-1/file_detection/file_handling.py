# file = open("filename", "mode")
# file = open("example.txt", "r")
# file = open("example.txt","w")
# file=open("example.txt", "a")
# file = open("example.txt", "rb")

# foo = open("foo.txt", "wb")
# print("name of the file: ", foo.name)
# print("closed or not: ", foo.closed)
# print("opening mode: ", foo.mode)
# foo.close()
# read()
# read()
# read()
# read()
# readline()
# readline()
# readline()
# readlines()
# readlines()

# with open("output.txt", 'r') as file:
#     content = file.read()
#     print(content)

# with open("output.txt", 'r') as file:
#     content = file.read()
#     print(content)

# with open("output.txt", 'r') as file:
#     content = file.readline()
#     print(content)


# with open("output.txt", 'r') as file:
#     content = file.readlines()
#     print(content)\

# with open("example.txt", 'r') as file:
#     line = file.readline()
#     while line:
#         print(line, end='')
#         line = file.readline()
# with open("example.txt", 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end='')

# with open("example.txt", "w") as file:
#     file.write("first writing in a file")
#     print("writing successfully")

# with open("example.txt", 'r') as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "a") as file:
#     file.write("new line added")

# lines = ["First line\n", "Second line\n", "Third line\n"]

# with open("example.txt", "w") as file:
#     file.writelines(lines)
#     print("content added successfully")

# file = open("example.txt", "w")
# file.write("this is an example")
# file.close()
# print("file closed successfully")

# with open("example.txt", "w") as file:
#     file.write("this is an example using the with statement")
#     print("file close successfully")

# try: 
#     file = open("example.txt", "w")
#     file.write("this an try finally example")
# finally:
#     file.close()
#     print("file close successfully")

# file = open("write.txt", "w")
# file.write("Hello World!")
# file.close()
# print("file opened successfully")

# file = open("write.txt", "a")
# file.write("\nAppending a new line.\n")
# file.close()
# print("new line appended successfully")

# with open("new.txt", "w") as file:
#     file.write("exact writing")
#     file.write("AGAIN WRITING")
# print("file wrote succeeded")

# lines = ["First line\n", "Second line\n", "Third line\n", "Fourth line\n"]

# with open("new.txt", "w") as file:
#     file.writelines(lines)

# print("file written succeeded")

# fo = open("foo1.txt", "w")
# fo.write("python is a great language")
# fo.close()

# with open("text.bin","wb") as f:
#     data = b"Hello World"
#     f.write(data)

# with open("text.bin", "wb") as file:
#     data = "Hello world111".encode("utf-8")
#     file.write(data)

# fo = open("foo1.txt", "a")
# text = "\n New python features"
# fo.write(text)
# fo.close()

# fo = open("foo1.txt", "w+")
# fo.write("this is a rat race")
# fo.seek(10, 0)
# data = fo.read(3)
# fo.seek(10,0)
# fo.write('cat')
# fo.close()

# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("example.txt", "r")
# line = file.readline()
# print(line)
# file.close()

# file = open("example.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print(line, end="")
# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("text.bin", "wb") as file:
#     data = b"Hello world-2"
#     file.write(data)

# with open("text.bin", "rb") as file:
#     data = file.read()
#     print(data.decode("utf-8"))

# n = 25
# data = n.to_bytes(9, 'big')
# with open("test.bin", "wb") as file:
#     file.write(data)

# with open("test.bin", "rb") as file:
#     data = file.read()
#     n = int.from_bytes(data, "big")
#     print(n)

# import struct
# x = 23.50
# data = struct.pack("f", x)
# with open("test.bin", "wb") as file:
#     file.write(data)

# import struct
# with open("test.bin", "rb") as file:
#     data = file.read()
#     x = struct.unpack("f", data)[0]
#     print(x)

# with open("foo1.txt", "r+") as fo:
#     fo.seek(10, 0)
#     data = fo.read(3)
#     print(data)

# import os
# current_name = "example.txt"
# new_name = "example1.txt"
# os.rename(current_name, new_name)
# print(f"File '{current_name}' renamed to '{new_name}' successfully")

# import os
# current_name = "example1.txt"
# new_name = "new_example.txt"
# os.rename(current_name, new_name)
# print(f"File -'{current_name}' has been renamed to '{new_name}' successfully")

# import os
# os.remove("foo.txt")
# os.remove("foo1.txt")

# import os
# file_to_delete = "file_to_delete.txt"
# os.remove(file_to_delete)
# print(f"File '{file_to_delete} has deleted'")

# import os 
# os.remove("new.txt")

# import os
# directory_path = "G:\\Desktop\\timekeeper"
# if os.path.exists(directory_path):
#     print(f"The directory '{directory_path}' exists.")
# else:
#     print(f"The directory '{directory_path}' does not exist")

# import os
# new_directory = "new_dir.txt"
# try:
#     os.makedirs(new_directory)
# except OSError as e:
#     print(f"Error: Failed to create directory '{new_directory}'. {e}")

# import os
# directory_path = "G:\\Desktop\\password.txt"
# if os.path.exists(directory_path):
#     print(f"The directory '{directory_path}' exists.")
# else:
#     print(f"The directory '{directory_path}' does not exist.")

# import os 
# new_directory = "newDir.txt"
# try:
#     os.makedirs(new_directory)
#     print(f"new directory '{new_directory}' created")
# except OSError as e:
#     print(f"Error: Failed to create directory  '{new_directory}' ")

# import os
# os.mkdir('test')
# print("directory created successfully")

# import os
# os.getcwd()

# import os
# current_directory = os.getcwd()
# print(f"Current directory '{current_directory}'")

# import os
# directory_path= r"G:\\Desktop\\python"
# try:
#     contents = os.listdir(directory_path)
#     print(f"Contents of '{directory_path}'")
#     for item in contents:
#         print(item)
# except OSError as e:
#     print(f"Error: failed to list contents of directory '{directory_path}'.{e}")



