# import math
# print("square root of 100: ", math.sqrt(100))
# print(math.sqrt(10))
# print(math.sqrt(20))
# print(math.sqrt(24))
# print(math.sqrt(8))
"this is the docstring of this file"
def SayHello(name):
    print("Hi {}! How are you?".format(name))
    return


def sum(x, y):
    return x + y

# print("sum: ", sum(10, 20))


def average(x, y):
    return (x + y) / 2


def power(x, y):
    return x ** y

if __name__ == "__main__":
    print("sum: ", sum(10, 20))
