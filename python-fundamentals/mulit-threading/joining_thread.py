from threading import Thread
from time import sleep

def my_function1(arg):
    for i in range(arg):
        print("child thread 1 running", i)
        sleep(0.5)
def my_function2(arg):
    for i in range(arg):
        print("child thread 2 running", i)
        sleep(0.1)

thread1 = Thread(target=my_function1, args=(5, ))
thread2 = Thread(target=my_function2, args=(3, ))

thread1.start()
thread1.join(timeout=0.2)

thread2.start()
thread2.join()

print("main thread finished...exiting")

