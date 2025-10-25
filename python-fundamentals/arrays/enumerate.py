fruitList = ["mango", "apple", "cherry", "banana"]
# for index, item in enumerate(fruitList):
#     print(f"{index} - {item}")

# newList = list(enumerate(fruitList, start=1))
# print(newList)

# for index, item in enumerate(fruitList, 1):
#     print(f"{index} - {item}")

fruits = [(8, "Grapes"), (10, "Apple"), (9, "Banana"), (12, "Kiwi")]
for index, (quantity, fruit) in enumerate(fruits):
    print(f"Index: {index}: Quantity: {quantity} - Fruit: {fruit}")
