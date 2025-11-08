import random

dice_drawing = {
    1: (
        " __________",
        "|          |",
        "|    1     |",
        "|     ●    |",
        "|          |",
        "|__________|",
    ),
    2: (
        " __________",
        "|          |",
        "|       ●  |",
        "|    2     |",
        "|  ●       |",
        "|__________|",
    ),
    3: (
        " __________",
        "|          |",
        "|   3  ●   |",
        "|    ●     |",
        "|  ●       |",
        "|__________|",
    ),
    4: (
        " __________",
        "|          |",
        "|  ●    ●  |",
        "|    4     |",
        "|  ●    ●  |",
        "|__________|",
    ),
    5: (
        " __________",
        "|          |",
        "|  ● 5  ●  |",
        "|    ●     |",
        "|  ●    ●  |",
        "|__________|",
    ),
    6: (
        " __________",
        "|          |",
        "|  ●    ●  |",
        "|  ●  6 ●  |",
        "|  ●    ●  |",
        "|__________|",
    ),
}


def roll_dice():
    roll = input("Roll the dice? (y/n) : ")
    while roll.lower() == "y".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        roll = input("\nRoll again? (y/n): ")


if __name__ == "__main__":
    roll_dice()
