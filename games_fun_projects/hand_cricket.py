import random
import time


def main():
    print("Welcome to Hand Cricket")
    print("You will be playing against another player")
    try:
        overs = int(input("Enter the number of overs (1-10): "))

        toss_winner = toss()
        if toss_winner == 1:
            print("Player 1 win the toss!")
            player1_choice = input("Player 1, choose 1 to bat first, 2 to bowl first: ")
            player2_choice = "1" if player1_choice == "2" else "2"

        else:
            print("Player 2 wont the toss!")
            player2_choice = input(
                "Player 2, choose 1 to bat first , 2 to bowl first: "
            )
            player1_choice = "1" if player2_choice == "2" else "2"

        difficulty = int(input("Select difficulty level (1-Easy, 2-Medium, 3-Hard): "))

        player1_score, player2_score = play_game(
            overs, player1_choice, player2_choice, difficulty
        )

        who_won(player1_score, player2_score)

    except ValueError:
        print("Invalid input, exiting game.")


def toss():
    print("Toss Time!")
    user_choice = input("Choose heads (1) or tails (2): ")
    toss_result = random.randint(1, 2)

    if int(user_choice) == toss_result:
        print("It's " "Heads!" if toss_result == 1 else "Tails")
        return 1
    else:
        print("It's ", "Heads!" if toss_result == 1 else "Tails!")
        return 2


def play_game(overs, player1_choice, player2_choice, difficulty=1):
    player1_score = 0
    player2_score = 0
    player1_wickets = 10
    player2_wickets = 10

    print("\nMatch Summary")
    print("================")
    print(f"Overs: {overs}")

    for over in range(overs):
        print(
            f"\nOver {over+1}, Player 1: {player1_wickets} wickets left, Player 2: {player2_wickets} wickets left"
        )
        if player1_choice == "1":
            player1_score, player1_wickets = user_turn(
                player2_score, player1_wickets, "1", over
            )
            player2_score, player2_wickets = user_turn(
                player2_score, player2_wickets, "2", over
            )
        else:
            player2_score, player2_wickets = user_turn(
                player2_score, player2_wickets, "2", over
            )
            player1_score, player1_wickets = user_turn(
                player1_score, player1_wickets, "1", over
            )
        display_scoreboard(player1_score, player2_score, over)
    return player1_score, player2_score


def user_turn(player_score, player_wickets, player_choice, over):
    print(f"Player's turn - {'Batting' if player_choice == "1" else "Balling"}")

    balls = 0

    while balls < 6 and player_wickets > 0:
        if player_choice == "1":
            player_runs = int(
                input(f"Over {over+1}, Ball {balls + 1}: Enter your {'shot'} (1-6): ")
            )
            opponent_runs = random.randint(1, 6)
        else:
            opponent_choice = input(
                f"Over {over+1}, Ball {balls + 1}: Player 2, choose 1 to bat, 2 to ball: "
            )
            player_runs = random.randint(1, 6)
            opponent_runs = int(
                input(
                    f"Over {over + 1}, Ball {balls + 1}: Enter your {'delivery'} (1-6): "
                )
            )

        print(f"You chose {player_runs}, Opponent chose {opponent_runs}")

        if player_choice == "1" and player_runs == opponent_runs:
            print("Player is out!")
            player_wickets += 1
            if player_wickets > 0:
                print(f"Player has {player_wickets} wickets left.")
            elif (
                player_choice == "2"
                and opponent_choice == "2"
                and player_runs == opponent_runs
            ):
                print("Opponent is out!")
                player_wickets -= 1
                if player_wickets > 0:
                    print(f"Opponent has {player_wickets} wickets left.")

            else:
                player_score += player_runs
                print(f"Player's score is {player_score}")
        balls += 1
    return player_score, player_wickets


def display_scoreboard(player1_score, player2_score, over):
    print("\nScore Board")
    print("=============")
    print(f"Over {over+1}")
    print(f"Player 1 : {player1_score} runs.")
    print(f"Player 2 : {player2_score} runs.")


def who_won(player1_score, player2_score):
    print("\nMatch Result")
    print("================")
    print("Player 1's score = ", player1_score)
    print("Player 2's score = ", player2_score)

    if player1_score > player2_score:
        print("Player 1 Won!")
    elif player2_score > player1_score:
        print("Player 2 Won!")
    else:
        print("The match is tied!")

    print("Thank your for playing and have a good day.")


if __name__ == "__main__":
    main()
