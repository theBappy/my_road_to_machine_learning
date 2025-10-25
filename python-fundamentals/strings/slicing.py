# var = "HELLO PYTHON"
# print(var[0])
# print(var[6])
# print(var[-1])
# print(var[12])

# print(var[3:8])
# print(var[-9:-4])
# print(var[:5])
# print(var[:4])
# print(var[6:])
# var[4] = "N"
# print(var)
# print(var[-12])
# print(var[-1])
# print(var[0])
# print(var[-3])
# print(var[::-1])
# var = "HELLO PYTHON"
# print(var[:6][:2])
# var1 = var[:6]
# print(var1)
# print(var1[:2])
# print(var[:])
# print(var[::-1])
# print(var[0:12])
# print(var[7:0])

# s1 = "WORD"
# print("Original string: ", s1)
# l1 = list(s1)
# print(l1)
# l1.insert(3,"L")
# print(l1)
# s1=''.join(l1)
# print(s1)

# s1 = "WORD"
# print(s1)
# l1 = list(s1)
# print(l1)
# l1.insert(3, "L")
# print(l1)
# new_string = ''.join(l1)
# print(new_string)

# s1 = "LIEUTENANT"
# print(s1)
# l1 = list(s1)
# print(l1)
# l1.insert(0, "i")
# print(l1)
# c1 = ''.join(l1)
# print(c1)

# import array as ar
# s1 ="WORD"
# print("original string: ", s1)
# sar = ar.array("u", s1)
# sar.insert(3, "L")
# s1 = sar.tounicode()
# print(s1)

import io

s1 = "WORD"
print("Original string: ", s1)

sio = io.StringIO(s1)
print(sio)
sio.seek(3)
print(sio.seek(3))
sio.write("LD")
s1 = sio.getvalue()
print(s1)