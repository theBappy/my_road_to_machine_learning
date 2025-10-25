# file = open("example.txt", "r")
# content = file.read()
# print(content)
# file.close()

# file = open("example.txt", "r")
# content = file.readline()
# print(content)
# file.close()

# file = open("foo.txt", "r")
# content = file.readlines()
# for line in content:
#     print(line, end="")
# file.close()

# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("example.txt", "wb") as file:
#     data = b"Hello World"
#     file.write(data)

# with open("text.bin", "rb") as file:
#     data = file.read()
#     print(data.decode(encoding="utf-8"))

# with open("example.txt", "rb") as file:
#     data = file.read()
#     print(data.decode(encoding="utf-8"))

# n= 25
# data = n.to_bytes(9, 'big')
# with open("test.bin","wb") as file:
#     file.write(data)

# n = 90
# data=n.to_bytes(8, 'big')
# with open("another.bin", "wb") as file:
#     file.write(data)

# with open("test.bin", "rb") as file:
#     data = file.read()
#     i = int.from_bytes(data, 'big')
#     print(i)

# with open("another.bin", "rb") as file:
#     data = file.read()
#     output = int.from_bytes(data, "big")
#     print(output)

# import struct
# x = 25.75
# data = struct.pack('f', x)
# with open("test.bin", "wb") as f:
#     f.write(data)

# import struct

# with open("test.bin", 'rb') as file:
#     data = file.read()
#     x = struct.unpack('f', data)[0]
#     print(x)

# with open("foo.txt", "r+") as fo:
    # fo.seek(0, 0)
    # data = fo.read(5)
    # print(data)

    # fo.seek(12, 0)
    # data = fo.read(5)
    # print(data)

    # fo.seek(16, 0)
    # data = fo.read(8)
    # print(data)

# with open("example.txt", "r+") as fo:
#     fo.write("This is a rat race")
#     fo.seek(0)
#     data = fo.read()
#     print(data)

fo = open("foo.txt", "w+")
fo.write("This a is cat race")
fo.seek(10, 0)
data = fo.read(3)
print(data)
fo.seek(10, 0)

fo.write("mouse")
fo.seek(0, 0)
data = fo.read()
print(data)
fo.close()
