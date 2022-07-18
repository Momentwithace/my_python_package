import random


class Dice:
    def __init__(self, player_name):
        self.player_name = player_name

    def roll(self):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        return first_dice, second_dice
        #print(first_dice, second_dice)


Ace = Dice("Ace")
print(Ace.roll())
