import random

print()
print("""WELCOME TO ROCK
PAPER AND SCISSOR        
""")
count = 0
player_score = 0
computer_score = 0
while count < 3:
    print()
    player = input("Pick a digit between 1 -3 to make a throw: ")
    while not player.isdigit() or not 1 <= int(player) <= 3:
        player = input("""1 --> ROCK
2 --> PAPER
3 --> SCISSORS
""")

    if player.isdigit() == 1:
        print("You Picked Rock")
    elif player.isdigit() == 2:
        print("You Picked Paper")
    else:
        print("You Picked Scissors")

    computer = random.randint(1, 3)
    result = computer
    if result == 1:
        print("Computer Picked Rock")
    elif result == 2:
        print("Computer picked paper")
    else:
        print("Computer picked scissor")

    if computer == 1 and player == 3 or computer == 3 and player == 2 or computer == 2 and player == 1:
        print("COMPUTER WINS")
        computer_score += 1

    if computer == 1 and player == 1 or computer == 3 and player == 3 or computer == 2 and player == 2:
        print("DRAW")

    else:
        print("PLAYER WINS")
        player_score += 1

    count += 1
    print("player1 won " + str(player_score))
    print("computer won " + str(computer_score))
    # 1

# count = 0
# player_score = 0
# computer_score = 0
# while count <= 3:
#     player1 = input("PLAYER1 --> Pick Between 1 - 3 to Make a Throw: ")
#     while not player1.isdigit() or not 1 <= int(player1) <= 3:
#         print("Invalid Entry!, Try Again: ")
#         player1 = input("PLAYER1 --> Pick Between 1 - 3 to Make a Throw: ")
#     # if player1.isdigit() == 1:
#     #     print("Player1 --> You Picked Rock")
#     #     if player1.isdigit() == 2:
#     #         print("Player1 --> You Picked Paper")
#     #         if player1.isdigit() == 3:
#     #             print("Player1 --> You Picked Scissors")
#     match player1:
#         case 1:
#             print("You Picked Rock")
#         case 2:
#             print("You Picked Paper")
#         case 3:
#             print("You Picked Scissors")
#     game = [1, 2, 3]
#     rand_num = random.randint(0, 2)
#     computer = random[rand_num]
#
#     if computer == 1 and player1 == 3 or computer == 3 and player1 == 2 or computer == 2 and player1 == 1:
#         print("COMPUTER WINS")
#         computer_score += 1
#
#     if computer == 1 and player1 == 1 or computer == 3 and player1 == 3 or computer == 2 and player1 == 2:
#         print("DRAW")
#
#     else:
#         print("PLAYER WINS")
#         player_score += 1
#
#     count += 1
#
# print("player1 won " + str(player_score))
# print("computer won " + str(computer_score))
