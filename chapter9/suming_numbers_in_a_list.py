# using for loop to get the sum of numbers in a list
numbers = [23, 45, 56, 67, 1]
total = 0
for number in numbers:
    total = total + number
print(total)

# using built-in function to sum the numbers in a list
numbers = [23, 45, 56, 67, 1]
print(sum(numbers))

# using list comprehension
print(f"Sum of this {[23, 45, 56, 67, 1]} is {sum([23, 45, 56, 67, 1])}")