numbers = [5, 2, 5, 2, 2]
for number in numbers:
    print("x" * number)
print()
# using nested for loop
# this program will print an F
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    output = ' '
    for num in range(number):
        output += 'x'
    print(output)


# this program will print an L
print()
numbers = [1, 1, 1, 1, 5]
for number in numbers:
    output = ' '
    for num in range(number):
        output += 'x'
    print(output)