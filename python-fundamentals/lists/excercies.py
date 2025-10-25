# L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
# L2 = []
# for x in L1:
#     if x not in L2:
#         L2.append(x)
# print(L2)

# numbers = [1, 9, 1, 6, 3, 4]
# total = 0
# for num in numbers:
#     total += num
# print(total)

import random
L1=[]
for x in range(5):
    x = random.randint(0, 100)
    L1.append(x)
print(L1)