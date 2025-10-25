# try:
#     open("no_file.txt")
# except OSError:
#     raise RuntimeError("unable to handle error")

# try:
#     open("no_file.txt")
# except OSError as exc:
#     raise RuntimeError from exc

# try:
#     open('no_file.txt')
# except OSError as exc:
#     raise RuntimeError from None

try: 
    try:
        raise ValueError("ValueError")
    except ValueError as e1:
        raise TypeError("TypeError") from e1
except TypeError as e2:
    print("The exception was", repr(e2))
    print("Its __context__ was", repr(e2.__context__))
    print("Its __cause__ was", repr(e2.__cause__))