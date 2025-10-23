from time import sleep

duration = int(input("Enter the duration in seconds: "))

count = 0
while count < duration:
    print(count, end="\r")
    sleep(1)
    count += 1

print("Your time is up!")