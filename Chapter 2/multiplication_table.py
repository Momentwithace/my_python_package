import itertools

print("MULTIPLICATION TABLE")
for number, multiplier in itertools.product(range(1, 13), range(1, 13)):
    print("{:3d}  * {:>3d}   = {:5d}".format(number, multiplier, number * multiplier))
    if multiplier == 12:
        print()