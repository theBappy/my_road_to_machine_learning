# def divide(a, b):
#     if b == 0:
#         raise ValueError("Cannot divide by zero")
#     return a / b
# try:
#     result = divide(10, 0)
# except ValueError as e:
#     print(e)

# class InvalidAgeError(Exception):
#     def __init__(self, age, message ="Age must be between 18 and 100"):
#         self.age = age
#         self.message = message
#         super().__init__(self.message)

# def set_age(age):
#     if age < 18 or age > 100:
#         raise InvalidAgeError(age)
#     print(f"Age is set to {age}")

# try:
#     set_age(150)
# except InvalidAgeError as e:
#     print(f"Invalid age: {e.age} - {e.message}")

def process_file(filename):
    try:
        with open(filename, "r") as file:
            data = file.read()
    except FileNotFoundError as e:
        print(f"File not found: {filename}")
        raise
try:
    process_file("nonexistentfile.txt")
except FileNotFoundError as e:
    print("Handling the exception at a higher level")