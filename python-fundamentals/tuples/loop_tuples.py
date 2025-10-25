# tup = (25, 12, 10, -21, 10, 100)
# for num in tup:
#     print(num, end="\n")

# my_tup = (1,2,3,4,5)
# index = 0
# while index < len(my_tup):
#     print(my_tup[index])
#     index += 1

tup = (25, 12, 10, -21, 10, 100)
indices = len(tup)
for i in range(indices):
    print("tup-[{}]".format(i), tup[i])
