# def printInfo(name, age):
#     print("Name: ", name)
#     print("Age: ", age)
#     return
# printInfo("Jenny", 29)
# printInfo(name="John",age=45)

# def division(num, den):
#     quotient = num / den
#     print("num:{} den:{} quotient:{}".format(num, den, quotient))
# division(10, 5)
# division(20,10)
# division(num=50, den=5)
# division(den=2, num=30)
# division(8, num=40)


#################### Keyword-only arguments
# force the function to accept argument as keyword only by using (*) before the arg
# print("Hello", "World",sep="-")
# print("Hello", "World", "-")

# def intr(amt, *, rate):
#     val = amt*rate / 100
#     return val
# interest = intr(1000, rate=10)
# print(interest)

# def intr(amount, *, rate):
#     val = amount * rate / 100
#     return val
# interest = intr(1000, rate=10)
# print(interest)