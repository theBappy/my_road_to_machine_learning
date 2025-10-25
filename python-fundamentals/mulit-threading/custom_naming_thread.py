import threading

def addition_of_numbers(x, y):
    print("This thread name: ", threading.current_thread().name)
    result = x + y

def cube_number(i):
    result = i ** 3
    print("This thread name: ", threading.current_thread().name)

def basic_function():
    print("This thread name: ", threading.current_thread().name)

t1 = threading.Thread(target=addition_of_numbers, name="My_Customer_Thread_Name", args=(2, 4))
t2 = threading.Thread(target=cube_number, args=(4, ))
t3 = threading.Thread(target=basic_function)


t1.start()
t1.join()

t2.start()
t2.join()

t3.name = "custom_name_2"
t3.start()
t3.join()

print(threading.current_thread().name)
