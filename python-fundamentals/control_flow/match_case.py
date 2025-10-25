# def weekday(n):
#     match n:
#         case 0: return "Monday"
#         case 1: return "Tuesday"
#         case 2: return "Wednesday"
#         case 3: return "Thursday"
#         case 4: return "Friday"
#         case 5: return "Saturday"
#         case 6: return "Sunday"
#         case _: return "Invalid day number"
# print(weekday(0))
# print(weekday(4))
# print(weekday(6))
# print(weekday(10))

# def access(user):
#     match user:
#         case "admin" | "manager": return "Full access"
#         case "guest": return "Limited access"
#         case _: return "No access"
# print(access("admin"))
# print(access('guest'))
# print(access("student"))


# def greeting(details):
#     match details:
#         case [time, name]:
#             return f"Good {time} {name}!"
#         case [time, *names]:
#             msg = ""
#             for name in names:
#                 msg += f"Good {time} {name}"
#             return msg
# print(greeting(["Morning", "John"]))
# print(greeting(["Afternoon", "John", "Jenny", "David"]))


# def greeting(details):
#     match details:
#         case [time, name]:
#             return f"Good {time} {name}!"
#         case [time, *names]:
#             msg = ""
#             for name in names:
#                 msg += f"Good {time} {name}\n"
#             return msg
# print(greeting(["Morning", "David"]))
# print(greeting(["Morning", "David", "Bappy", "John", "Harry"]))


def intr(details):
    match details:
        case [amount, duration] if amount < 10000:
            return amount * 10 * duration / 100
        case [amount, duration] if amount > 10000:
            return amount * 15 * duration/100
print("Interest = ", intr([7500, 5]))
print("Interest = ", intr([17500, 3]))