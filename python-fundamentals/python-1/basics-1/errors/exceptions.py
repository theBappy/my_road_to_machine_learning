# try:
#     fh = open("testfile", "w")
#     fh.write("this is my test file for exception handling")
# except IOError:
#     print("Error: can\'t find file or read data")
# else: 
#     print("Written content in the file succeeded")
#     fh.close()

# try:
#     fh = open("testfile", "r")
#     fh.write("this is another test file for exception handling")
# except IOError:
#     print("Error: can\'t find file or read data")
# else:
#     print("succeeded")

# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("this is test file")
#     finally:
#         print("going to close the file")
#         fh.close()
# except IOError:
#     print("Error: can\'t find file or read data")

# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError as Argument:
#         print("the argument does not contain numbers\n", Argument)
# temp_convert("xyz")

# def functionName(level):
#     if level < 1:
#         raise "Invalid level!", level
