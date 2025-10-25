# try:
#     fh = open("testfile", "w")
#     fh.write("this is my test file")
# finally:
#     print("Error: can\'t find the file to write data")
#     fh.close()


# try:
#     fh = open("testfile", "w")
#     try:
#         fh.write("this is the test file")
#     finally:
#         print("going to close the file")
#         fh.close()
# except IOError:
#     print("Error: can\'t find the file to write")

def temp_converter(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("The argument does not contains numbers\n", Argument)
temp_converter("xyz")