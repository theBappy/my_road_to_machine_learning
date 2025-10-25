# is_nice = True
# print("nice" if is_nice else "not nice")

# nice = True
# personality = ("mean", "nice")[nice]
# print("The cat is", personality)

# num = 17
# print("Even number" if num % 2 == 0 else "Odd Number")

# signal = "green light"
# print("move" if signal == "green light" else "stop") 

# def get_fee(is_number):
#     return 10 if is_number else 0
# print(get_fee(False))

# def get_free(is_number):
#     return 10 if is_number else 0
# print(get_free(True))

# signal = "green light"
# action = ("move", "stop")[signal == 'green light']
# print(action)

# signal = "green light"
# action = ("stop", "move")[signal == 'green light']
# print(action)

# signal = 'green light'
# action = ("stop", "move")[signal == 'green light']
# print(action)

# signal = "green light"
# action = ["stop", "move"][signal == 'green light']
# print(action)

# signal = "red light"
# action = {False: "stop", True: "move"}[signal == 'red light']
# print(action)

# double = lambda x: x * 2

# signal= "green light"
# action = (lambda msg: f"stop {msg}", lambda msg: f"move {msg}")[signal == 'green light']("now")
# print(action)

# print("move" if signal == 'green light' else "stop") 

# signal = "black light"
# action = "move" if signal == 'green light' else "stop" if signal == 'red light' else "Invalid signal"
# print(action) 

# n = 5
# print("even" if n % 2 == 0 else "odd")

# n = 5
# print("positive" if n > 0 else "negative" if n < 0 else "zero")

# n = 7
# res = ("Odd", "Even")[n % 2 == 0]
# print(res)
# a = 10
# b = 20
# max = {True: a, False: b}[a > b]
# print(max)
# a = 10
# b = 20
# max = (lambda x, y:  x if x > y else y)(a,b)
# print(max)
a= 10
b = 20
max = (lambda x, y: x if x > y else y)(a, b)
print(max)
min = (lambda x, y: x if x < y else y)(a,b)
print(min)