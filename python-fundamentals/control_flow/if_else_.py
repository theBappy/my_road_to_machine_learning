# discount = 0
# amount = float(input("Enter your buying amount of todays: "))

# if amount > 1000:
#     discount = amount * 5 / 100

# print("You have to pay: ", amount - discount)

# age = int(input("How old are you?: "))
# if 18 <= age < 75:
#     print("You are eligible to vote")
# elif age > 75:
#     print("You are too old to vote")
# else:
#     print("You are too kid to vote")

# amount = float(input("Enter amount: "))
# print("Amount: ", amount)

# if amount > 10000:
#     discount = amount * 20 / 100
# else:
#     if amount > 5000:
#         discount = amount * 10 / 100
#     else:
#         if amount > 1000:
#             discount = amount * 5 / 1000
#         else:
#             discount = 0

# print("Payable amount: ", amount - discount)

amount = float(input("Enter amount: "))
print("Amount: ", amount)
if amount >= 10000:
    discount = amount * 10 / 100
elif amount >= 5000:
    discount = amount * 5 / 1000
elif amount >= 3000:
    discount = amount * 3/100
else:
    discount = 0
print("Payable amount: ", amount - discount)

