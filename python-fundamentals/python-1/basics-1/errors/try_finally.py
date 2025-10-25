# try:
#     fh = open("testfile", "w")
#     fh.write("this is the test file with try finally")
# finally:
#     print("Error: can\'t find file or read data")
#     fh.close()

# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("this is the test fil")
#     finally:
#         print("Going to close the file")
#         fh.close()
# except IOError:
#     print("Error: can\'t find file or read data")

def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contain numbers\n", Argument)
temp_convert("xyz")
