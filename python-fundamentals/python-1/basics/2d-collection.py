# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "beef", "turkey"]

# groceries = [
#     ["apple", "orange", "banana", "coconut"],
#     ["celery", "carrots", "potatoes"],
#     ["chicken", "fish", "beef", "turkey"]
# ]

# print(groceries[0][0])

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

# 2-d keypad
# num_pad = (
#     (1, 2, 3), 
#     (4, 5, 6), 
#     (7, 8, 9), 
#     ('*','0','#')
# )

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()


num_pad = (
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ("*","0","#"),
)
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
