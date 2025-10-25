import threading
def func(x):
    print("Current thread details: ", threading.current_thread())
    for n in range(x):
        print('{} Running'.format(threading.current_thread().name), n)
        print("Internal thread finished...")
# creating threads objects
t1 = threading.Thread(target=func, args=(2, ))
t2 = threading.Thread(target=func, args=(3, ))

print("Thread state: CREATED")
t1.start()
t2.start()

# wait for threads to complete
t1.join()
t2.join()
print("Threads state: FINISHED")

# simulate main thread work
for i in range(3):
    print("Main thread running", i)

print("Main thread finished")
