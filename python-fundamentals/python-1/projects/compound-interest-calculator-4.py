

principle = 0
rate = 0
time = 0


while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle cant' be less than zero")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if principle < 0:
        print("Interest rate cant' be less than zero")
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time cant' be negative")
    else:
        break

total = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total:.2f}")


principle = 0
rate = 0
time = 0
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle can't be less than zero")
    else:
        break
while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate can't be negative")
    else:
        break
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("Time can't be negative in years")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

