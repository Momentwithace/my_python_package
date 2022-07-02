numbers = ((1, 2), (3, 4))
print(type(numbers))
print(numbers)

sum_ = 0
for num in numbers:
    sum_ = sum(num)
    print(sum_)
    print(f"Row 1 sum: {sum_}")
