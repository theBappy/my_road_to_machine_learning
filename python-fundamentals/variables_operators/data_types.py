# var1 = 1
# var2 = True
# var3 = 10.45
# var4 = 10 + 3j
# print(type(var4))

# a = 100
# print(type(a))
# print(type(2.45))
# print(type(5+4j))
# print(type("Hello World"))

# str = "Hello World"
# print(str)
# print(str[0])
# print(str[1:5])
# print(str[-1])
# print(str[::-1])
# print(str[:-5])
# print(str * 2)
# print(str + " Test")

# list = ['abcd', 786, 2.23, 'john', 70.3, True]
# print(list)
# print(list[0])
# print(list[:-1])
# print(list[::-1])
# print(list[2:])
# print(list* 2)
# print(list + list)

# tuple = ("abcd", 758, 2.25, True, 70.79)
# print(tuple)
# print(tuple[0])
# print(tuple[::-1])
# print(tuple[1:])
# print(tuple[1:-2])
# print(tuple * 2)
# print(tuple + tuple)

# range(start, stop, step)

# for i in range(5):
#     print(i)

# for i in range(2, 5):
#     print(i)

# for i in range(1, 5, 2):
#     print(i)

# b1 = bytes([65, 66, 67, 68, 69])
# print(b1)
# b2 = b"Hello"
# print(b2)

# value = bytearray([72, 101, 108, 108, 111])
# print(value)

# val = bytearray("Hello","utf-8")
# print(val)

# data = bytearray(b'Hello ,World!')
# view = memoryview(data)
# print(view)

# import array
# arr = array.array('i', [1,2,3,4,5])
# view = memoryview(arr)
# print(view)

# data = b'Hello, World!'
# view = memoryview(data[7:])
# print(view)

# dict = {}
# dict['one'] = "This is one"
# dict['two'] = "This is two"
# tinydict = {"name": "John", "code":6743, "dept": "sales"}
# print(dict['one'])
# print(dict['two'])
# print(tinydict)
# print(tinydict.keys())
# print(tinydict.values())
# print(tinydict.items())
# print(type({2023, "Python", 3.11, 5+6j, 1.23E-4}))

# my_set = {123, 456, 5, 6}
# my_set2 = {"Java", "Python", "JavaScript"}
# print(my_set)
# print(my_set2)
# a = 2
# b = 4
# print(bool(a==b))
# print(a==b)
# a = None
# print(bool(a))
# a= ()
# print(bool(a))
# a =0.0
# print(bool(a))
# a= 10
# print(bool(a))
# x = None
# print("x = ", x)
# print("Type of x = ", type(x))

# print("Conversion to integer data type")
# a = int(1)
# b = int(2.2)
# c = int("3.3")
# print(a)
# print(b)
# print(c)

# a = float(1)
# b = float(2.2)
# c = float("3.3")
# print(a)
# print(b)
# print(c)

a = str(1)
print(type(a))
print(a)