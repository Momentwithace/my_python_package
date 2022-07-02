import random


def coin_flip():
    if random.randint(0, 1) == 0:
        print("Head")
        return "Head"
    else:
        print("Tail")
        return "Tail"


head_flip = 0
tail_flip = 0

for flip in range(10):
    if coin_flip() == "Head":
        head_flip = head_flip + 1
    else:
        tail_flip = tail_flip + 1
total_tail_flip = tail_flip
total_head_flip = head_flip

print(head_flip)
print(tail_flip)
