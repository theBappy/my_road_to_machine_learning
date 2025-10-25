# def add(*args):
#     s = 0
#     for x in args:
#         s = s + x
#     return s
# # result = add(10, 20, 30, 40)
# # print(result)
# result = add(1,2,3)
# print(result)

# def avg(first, *rest):
#     second = max(first)
#     return (first + second) / 2
# result=avg(40,30,50,25)
# print(result)

# def avg(first, *rest):
#     second = max(rest)
#     return (first + second) / 2
# result = avg(40,30,50,25)
# print(result)

# def avg(first, *rest):
#     second = max(rest)
#     return (first + second) / 2
# result = avg(40, 50, 60, 80)
# print(result)

# def addr(**kwargs):
#     for k, v in kwargs.items():
#         print("{} : {}".format(k, v))
# print("pass two keyword args")
# addr(Name="John",City = "London")

# def addr(**kwargs):
#     for k,v in kwargs.items():
#         print("{} - {}".format(k,v))
# print("Pass two keyword args")
# addr(name="John", city="London")

# def addr(**kwargs):
#     for k, v in kwargs.items():
#         print("{}-{}".format(k,v))
# print("pass 4 keyword args")
# addr(name="John", age=34, city="London", ph_no="128828882")

def percent(math, sci, **optional):
    print("maths: ", math)
    print("sci: ", sci)
    s= math+sci
    for k, v in optional.items():
        print("{}:{}".format(k,v))
        s = s + v
    return s/ (len(optional) / 2)

result = percent(math=80, sci = 75, eng=70, hist = 67, geo= 72)
print(result)
