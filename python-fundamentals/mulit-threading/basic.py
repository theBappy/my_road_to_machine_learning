# import _thread
# import time
# def print_name(name, *arg):
#     print(name, *arg)
# name = "TutorialPoints..."
# _thread.start_new_thread(print_name, (name, 1))
# _thread.start_new_thread(print_name, (name, 1, 2))
# time.sleep(1)

# import threading
# import time
# def print_name(name, *args):
#     print(name, *args)

# name = "John Doe..."
# thread1 = threading.Thread(target=print_name, args=(name,1))
# thread2 = threading.Thread(target=print_name, args=(name,1, 2))

# thread1.start()
# thread2.start()

# # waits for the thread to complete
# thread1.join()
# thread2.join()

# print("threads are finished...exiting")

import threading
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      # Get lock to synchronize threads
      threadLock.acquire()
      print_time(self.name, self.counter, 3)
      # Free lock to release next thread
      threadLock.release()

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")
    