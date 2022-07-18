import random as ram


for i in range(3):
    ram.random()
    print(ram.randint(10, 20))

members = ["Ace", "Elon", "Zeddy", "Odugwo"]
leader = ram.choice(members)
print(leader)