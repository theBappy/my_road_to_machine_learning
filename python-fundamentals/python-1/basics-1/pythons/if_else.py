# discount = 0
# amount = 1200

# if amount > 1000:
#     discount = amount * 10 / 100
# print("amount: ", amount - discount)

# age = 25

# if age >= 18:
#     print("eligible to vote")
# elif age < 18:
#     print("not eligible to vote")
# else:
#     print("eligible to vote")

# amount = 2500
# print("Amount: ",amount)
# if amount > 10000:
#     discount = amount * 20 / 100
# else:
#     if amount > 5000:
#         discount = amount * 10 / 100
#     else:
#         if amount > 1000:
#             discount = amount * 5 / 100
#         else:
#             discount = 0

# print("Payable amount: ", amount - discount)

amount = 2500
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0

print('Payable amount = ',amount - discount)

