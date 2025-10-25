# print("Hello", "World", sep="-")
# print("Hi", "John", "-")

# def intr(amount, *, rate):
#     val = amount * rate/100
#     return val
# interest = intr(1000, rate=10)
# print(interest)

# def intr(amount, *, rate):
#     val = amount * rate / 100
#     return val
# interest = intr(1000, rate = 10)
# print(interest)

def info(name, age, *, id, role):
    print(f"{name} - {age} - {id} - {role}")
info("John", 23, id = 123, role="Student")