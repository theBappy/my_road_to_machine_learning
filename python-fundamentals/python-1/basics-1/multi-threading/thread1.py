# import _thread
# import time

# def print_name(name, *args):
#     print(name, *args)

# name = "TutorialsPoints"
# _thread.start_new_thread(print_name, (name, 1))
# _thread.start_new_thread(print_name, (name, 1, 2))

# time.sleep(5)

import threading
import time

def print_name(name, *args):
    print(name, *args)

name = "Hello World"

thread1 = threading.Thread(target=print_name, args=(name, 1))
thread2 = threading.Thread(target=print_name, args=(name, 1, 2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Threads are finished...exiting")