temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny 🥳")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 0 < temp < 28 and is_sunny:
    print("it is warm outside")
    print("it is sunny")

if temp >= 28 and not is_sunny:
    print("It is hot outside 🥵")
    print("It is cloudy 🥳")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy ")
elif 0 < temp < 28 and not is_sunny:
    print("it is warm outside")
    print("it is cloudy")
    

# temp = 20
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")