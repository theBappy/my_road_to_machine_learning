import os
import time

def shut_down():
    os.system("shutdown /s /t 1")

set_time = input("Shutdown After ==> ")
set_time = int(set_time)

sec = 60

print("Computer will shut down in " + str(set_time) + " Minutes.")
time.sleep(set_time * 60)
print("Computer will not shutdown!")
time.sleep(3)

if __name__ == "__main__":
    shut_down()