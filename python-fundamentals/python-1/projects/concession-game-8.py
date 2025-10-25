
menu = {
    "pizza": 3.80,
    "popcorn": 4.25,
    "coffee": 5.00,
    "chocolate": 7.75,
    "burger": 9.50,
    "chips": 2.50,
    "fries": 12.75,
    "nachos": 15.00,
}
cart = []
total = 0

print("---------------- MENU -----------------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}")

print("---------------- ---- -----------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------- YOUR ORDER -----------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")

# menu = {
#     "pizza": 3.80,
#     "popcorn": 4.25,
#     "coffee": 5.00,
#     "chocolate": 7.75,
#     "burger": 9.50,
#     "chips": 2.50,
#     "fries": 12.75,
#     "nachos": 15.00,
# }
# cart = []
# total = 0
# print("-------------------MENU-----------------")
# for key, value in menu.items():
#     print(f"${key:10} - ${value:.2f}")
# print("----------------------------------------")
# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == 'q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
# print("-----------------YOUR ORDER----------------------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=' ')
# print()
# print(f"Total amount is: ${total:.2f}")