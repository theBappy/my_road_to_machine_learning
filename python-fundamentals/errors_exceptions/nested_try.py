# a = 10
# b = 0
# try:
#     print(a/b)
# except Exception:
#     print("General exception")
# finally:
#     print("inside outer finally block")

# a = 10
# b = 0
# try:
#     print(a/b)
#     try:
#         print("This in inner try block")
#     except Exception:
#         print("General exception")
#     finally:
#         print("inside inner finally block")

# except ZeroDivisionError:
#     print("Division by 0")
# finally:
#     print("inside outer finally block")

# a = 10
# b = 0
# try:
#     print("this is outer try block")
#     try: 
#         print(a/b)
#     except ZeroDivisionError:
#         print("division by 0")
#     finally:
#         print("inside inner finally block")
# except Exception:
#     print("General exception")
# finally:
#     print("inside outer finally block")


a = 10
b = 0
try:
    print("this is outer try block")
    try:
        print(a/b)
    except KeyError:
        print("Key error")
    finally:
        print("inside inner finally block")

except ZeroDivisionError:
    print("division by 0")
finally:
    print("inside outer finally block")