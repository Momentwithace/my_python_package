import random
correct_score = random.randint(0, 10)
count = 0
while count < 3:
    count += 1
    guess = int(input("guess a number between 0 - 10: \n"))
    if guess < correct_score:
        print("Too low, try again!")
    elif guess > correct_score:
        print("Too high, try again!")
    else:
        print("Awesome, You're doing well!")
        break

else:
    print("You're tired!, you can never make it")
