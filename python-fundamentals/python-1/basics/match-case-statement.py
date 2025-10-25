
# Match-case statement(switch case): An alternative to using many 'elif' statements, execute some code if a value matches a 'case', Benefits: code is cleaner and syntax is more readable

# def day_of_week(day):
#     match day:
#         case 1:
#             return "Sunday"
#         case 2:
#             return "Monday"
#         case 3:
#             return "Tuesday"
#         case 4:
#             return "Wednesday"
#         case 5:
#             return "Thursday"
#         case 6:
#             return "Friday"
#         case 7:
#             return "Saturday"
#         case _: # '_' wild card [no matching case]
#             return "Not a valid day"
# print(day_of_week("pizza"))

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        # case "Tuesday":
        #     return False
        # case "Wednesday":
        #     return False
        # case "Thursday":
        #     return False
        # case "Friday":
        #     return False
        # case "Saturday":
        #     return True
        case _:
            return False
        
print(is_weekend("Sunday"))
        
        
