from random import randint

print("Welcome to the Higher-Lower Game!")

r_num = randint(0, 100)

no_guesses = 0

while True:
    while True:
        guess = input("Guess the number: ")
        if guess.isdigit():
            integer_number = int(guess)
            print("You entered: ", integer_number)

            if integer_number > r_num:
                print("Lower")
            elif integer_number < r_num:
                print("Higher")
            else:
                (print("You win! The number is: " + guess + "!"), quit())
            no_guesses += 1

        else:
            print("Invalid input. Please enter an integer.")