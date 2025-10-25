# str1 = "HELLO"
# str2 = "WORLD"
# # print(str1 +" "+ str2)
# new_string = "HELLO"  * 3
# print(new_string)

# str1 = "Hello"
# str2 = "World"
# print("string 1: ", str1)
# print("string 2: ", str2)
# str3 = str1 + str2*3
# print(str3)
# print((str1+str3)*2)

# name = "Python"
# print("Welcome to %s!" % name)
# str = "Welcome to {}"
# print(str.format("Python"))

# item1 = 2500
# item2 = 300
# print(f"Total: {item1 + item2}")

# from string import Template

# str = "Hello and Welcome to $name !"
# templateObj = Template(str)
# new_str = templateObj.substitute(name="Python")
# print(new_str)

# normal_string = "Hel\nlo"
# print(normal_string)

# raw_string = r"Hello"
# print(raw_string)

# normal = "Hello\nWorld"
# print(normal)
# raw = r"Hello\nWorld"
# print(raw)

# s = 'This string not include \
#     backlashes or newline characters'
# print(s)
# s = s = 'The \\character is called backlash'
# print(s)
# s = 'Hello \'Python\''
# print(s)
# s = "Hello \"Python\""
# print(s)

# s = 'Hel\blo'
# print(s)
# s='Hello\a'
# print(s)

# s = 'Hello\nPython'
# print(s)
# s = 'Hello\fWorld'
# print(s)
# s= "Hello\fPython"
# print(s)

# s = "\101"
# print(s)
# s = "\x41"
# print(s)

# str = "hello world"
# output = str.capitalize()
# print(output)

# str = "hii! welcome to python"
# output = str.capitalize()
# print(output)

# str = "hiiiii"
# output = str.capitalize()
# print(output)

# str = "HELLO"
# output =str.casefold()
# print(output)

# str1 = "WORLD"
# result = str.casefold()
# print(result)

# str = "HELLO WORLD"
# output =str.casefold()
# print(output)

# str = "Hello, World"
# output = str.casefold()
# print(output)

# text1= "hello"
# text2 = "HELLO"
# result = text1.casefold() == text2.casefold()
# print(result)


# text = "Hèllò Wørld"
# output = text.casefold()
# print(output)

# str = "THIS IS STRING EXAMPLE"
# print(str.lower())

# str = "HELLO WORLD!"
# print(str.lower())

# str1 = "STRING EXAMPLE"
# str2 = "STRING example"
# print(str1.lower())
# print(str2.lower())

# if str1.lower() == str2.lower():
#     print("both strings are equal")
# else:
#     print("they are not equal")

# str = "HELLO WORLD"
# print(str.swapcase())

# my_str = "All animals are equal. Some are more equal"
# vowels = "aeiou"
# count = 0
# for x in my_str:
#     if x.lower() in vowels:
#         count += 1
# print("number of vowels: ", count)

# mystr = '10101'

# def strtoint(mystr):
#    for x in mystr:
#       if x not in '01': return "Error. String with non-binary characters"
#    num = int(mystr, 2)
#    return num
# print ("binary:{} integer: {}".format(mystr,strtoint(mystr)))

# digits = [str(x) for x in range(10)]
# my_str = "HE12llo, Py00th55on"
# chars = []
# for x in my_str:
#     if x not in digits:
#         chars.append(x)
# new_str = ''.join(chars)
# print(new_str)