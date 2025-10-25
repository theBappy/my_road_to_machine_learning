# def KelvinToFahrenheit(Temperature):
#     assert("Temperature >= 0"),"Colder than absolute zero!"
#     return ((Temperature-273)*1.8) + 32
# print(KelvinToFahrenheit(273))
# print(KelvinToFahrenheit(505.78))
# print(KelvinToFahrenheit(-5))

# try:
#     fh = open("testfile", "w")
#     fh.write("this is my test file for exception handling!")
# except IOError:
#     print("Error: can'\t find file or read data")
# else:
#     print("Written content in the file succeeded")
#     fh.close()

# try:
#     fh = open("testfile", "r")
#     fh.write("this is my test file for exception handling!")
# except IOError:
#     print("Error: can\'t find file or read data")
# else: 
#     print("succeeded")

# try:
#     fh = open("testfile", "w")
#     fh.write("this is my test file")
# finally:
#     print("error")

# try: 
#     fh=open("testfile", "w")
#     try:
#         fh.write("this is my test file")
#     finally:
#         print("going to close the file")
#         fh.close()
# except IOError:
#     print("Error")

# def temp_convert(var):
#     try:
#         return int(var)
#     except ValueError as Argument:
#         print("the argument does not contain numbers\n", Argument)
# temp_convert("xyz")

# def functionName(level):
#     if level < 1:
#         raise "Invalid level!", level

class NetworkError(RuntimeError):
    def __init__(self, arg):
        self.args = arg
try:
    raise NetworkError("Bad hostname")
except NetworkError as e:
    print(e.args)