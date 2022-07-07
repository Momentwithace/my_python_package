print("Welcome to Rock and Scissors")
print("""1 --> ROCK
2 --> PAPER
3 --> SCISSORS
""")


def game():
    print("""
    1 --> Play
    2 --> Rules
    3 --> Quit
    """)


def game():
    count = 0
    while count < 5:
        count += 1
        player1 = input("PLAYER1 --> Pick Between 1 - 3 to Make a Throw: ")
        while not player1.isdigit():
            print("Invalid Entry!, Try Again: ")
            player1 = input("PLAYER1 --> Pick Between 1 - 3 to Make a Throw: ")

        if player1.isdigit() == 1:
            print("Player1 --> You Picked Rocky")
            if player1.isdigit() == 2:
                print("Player1 --> You Picked Paper")
                if player1.isdigit() == 3:
                    print("Player1 --> You Picked Scissors")

        else:
            print("Pick Between 1 - 3 to Throw:")

        player2 = input("PLAYER2 --> Pick Between 1 - 3 to Throw: ")
        while not player2.isdigit():
            print("Invalid Entry!, Try Again: ")
            display = input("Pick Between 1 - 3 to Throw: ")

        if player2.isdigit() == 1:
            print("Player2 --> You Picked Rock_stone")
        if player2.isdigit() == 2:
            print("Player2 --> You Picked Paper")
        if player2.isdigit() == 3:
            print("Player2 --> You Picked Scissors")

        else:
            print("Pick Between 1 - 3 to Throw:")

    else:
        print("GAME OVER")


game()
