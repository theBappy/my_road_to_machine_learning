import random


options = ("rock", "paper", "scissors")

playing = True

while playing:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie")
    elif player == 'rock' and computer == 'scissors':
        print("Player win!")
    elif player == 'paper' and computer == 'rock':
        print("Player win!")
    elif player == 'scissors' and computer == 'paper':
        print("Player win!")
    else:
        print("Player lose!")

    # play_again = input("Play again? (y/n): ").lower()
    # if not play_again == 'y':
    #     playing = False

    if not input("Play again? (y/n) : ").lower() == "y":
        playing = False
    
print("Thanks for playing!!!")