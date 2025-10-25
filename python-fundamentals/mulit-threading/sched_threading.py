import sched
from datetime import datetime
import time

def addition(a, b):
    print("Performing addition: ", datetime.now())
    print("Time: ", time.monotonic())
    print("Result {} + {} = ".format(a,b), a + b)

s = sched.scheduler()

print("start time: ", datetime.now())

event1 = s.enter(4, 1, addition, argument=(5,6))

print("Event created: ", event1)
s.run()
print("End time: ", datetime.now())

