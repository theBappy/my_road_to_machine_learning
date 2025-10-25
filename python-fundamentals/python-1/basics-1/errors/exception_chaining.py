# try:
#     open("nofile.txt")
# except OSError:
#     raise RuntimeError("unable to handle error")

# try:
#     open("nofile.txt")
# except OSError:
#     raise RuntimeError from None

try:
    try:
        raise ValueError("ValueError")
    except ValueError as e1:
        raise TypeError("TypeError") from e1
except TypeError as e2:
    print("The exception was", repr(e2))
    print("The __context__ was", repr(e2.__context__))
    print("The __cause__ was", repr(e2.__cause__))