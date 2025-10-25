# d1 = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# keys = {"two","five"}
# d2 = {}
# for k in keys:
#     d2[k] = d1[k]
# print(d2)

# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
# l1 = list(d1.items())
# print(l1)

# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
# l1 = list(d1.items())
# print(l1)


d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
vals = list(d1.values())
uvals = [v for v in vals if vals.count(v) == 1]
d2 = {}
for k, v in d1.items():
    if v in vals:
        d = {k : v}
        d2.update(d)
print(d2)