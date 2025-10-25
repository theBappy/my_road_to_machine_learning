# Default arguments = A default value for certain parameters, default is used when that argument is omitted, make functions more flexible, reduces # of arguments 1.position 2. DEFAULT 3.keyword 4.arbitrary

# def net_price(list_price, discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

import time

def counter(end, start=25):
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")
counter(30)