import datetime

def get_time():
    return datetime.datetime.now()

def input_t(n):
    if n == 1:
        d = int(input("Enter 1 for exercise and 2 for food: "))
        if d == 1:
            value = input("type here...\n")
            with open("my_exercise.txt", "a") as file:
                file.write(str([str(get_time())]) + " : " + value + "\n ")
            print("Written successfully!")
        elif d == 2:
            value = input("type here.... \n")
            with open("my_food_list.txt", "a") as file:
                file.write(str([str(get_time())]) + " : " + value + "\n ")
            print("Written successfully")

    elif n == 2:
        d = int(input("Enter 1 for exercise and 2 for food: "))
        if d == 1:
            value = input("type here...\n")
            with open("david_exercise.txt", "a") as file:
                file.write(str([str(get_time())]) + " : " + value + "\n ")
            print("Written successfully")
        elif d == 2:
            value = input("type here... \n")
            with open("david_food.txt", "a") as file:
                file.write(str([str(get_time())]) + " : " + value + "\n ")
            print("Written successfully")
    elif n == 3:
        d = int(input("Enter 1 for exercise and 2 for food: "))
        if d == 1:
            value = input("type here...\n")
            with open("john_exercise.txt", "a") as file:
                file.write(str([str(get_time())]) + " : " + value + "\n ")
            print("Written successfully")
        elif d == 2:
            value = input("type here... \n")
            with open("john_food.txt", "a") as file:
                file.write(str([str(get_time())]) + " : " + value + "\n ")
            print("Written successfully")
    else:
        print("Enter the valid input 1(my) 2(david) 3(john)")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("my_exercise.txt") as file:
                for i in file:
                    print(i, end="")
        elif c == 2:
            with open("my_food_list.txt") as file:
                print(i, end="")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("david_exercise.txt") as file:
                for i in file:
                    print(i, end="")
        elif c == 2:
            with open("david_food.txt") as file:
                print(i, end="")
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("john_exercise.txt") as file:
                for i in file:
                    print(i, end="")
        elif c == 2:
            with open("john_food.txt") as file:
                print(i, end="")

    else:
        print("Plz enter valid input(my, david, john)")

print("Health Management System")
a = int(input("Press 1 for log the value and 2 for retrieve: "))

if a == 1:
    b = int(input("Press 1 for my, 2 for david and 3 for john: "))
    input_t(b)

else:
    b = int(input("Press 1 for my, 2 for david and 3 for john: "))
    retrieve(b)

    
        
