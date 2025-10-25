
# def week_day(n):
#     match n:
#         case 0: return 'Sunday'
#         case 1: return 'Monday'
#         case 2: return 'Tuesday'
#         case 3: return 'Wednesday'
#         case 4: return 'Thursday'
#         case 5: return 'Friday'
#         case 6: return 'Saturday'
#         case _: return "Invalid day number"
# print(week_day(3))
# print(week_day(5))
# print(week_day(0))
# print(week_day(10))

# def access(user):
#     match user:
#         case "admin" | "manager" | "ceo":
#             return "Full access"
#         case "guest":
#             return "Limited access"
#         case _: 
#             return "No access"
# print(access("guest"))
# print(access("admin"))
# print(access('john'))
# print(access('ceo'))

# def greeting(details):
#    match details:
#       case [time, name]:
#          return f'Good {time} {name}!'
#       case [time, *names]:
#          msg=''
#          for name in names:
#             msg+=f'Good {time} {name}!\n'
#          return msg
# print(greeting(["Morning", "Alex"]))
# print(greeting(["Night", "Guest"]))
# print(greeting(["Evening", "Clark", "Watson", "Ponting"]))

# def intr(details):
#    match details:
#       case [amount, duration] if amount<10000:
#          return amount*10*duration/100
#       case [amount, duration] if amount>=10000:
#          return amount*15*duration/100
# print ("Interest = ", intr([5000,5]))
# print ("Interest = ", intr([15000,3]))

# def is_weekend(day):
#     match day:
#         case "Saturday" | "Sunday":
#             return True
#         case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#             return False
#         # case "Tuesday":
#         #     return False
#         # case "Wednesday":
#         #     return False
#         # case "Thursday":
#         #     return False
#         # case "Friday":
#         #     return False
#         # case "Saturday":
#         #     return True
#         case _:
#             return False
        
# print(is_weekend("Sunday"))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return "It's a weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "It was a long tiring working day"
        case _:
            return "Invalid day"
        
print(is_weekend("Sunday"))
print(is_weekend("Tuesday"))
print(is_weekend("January"))
