def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min


mimi = find_min((8, 2, 3, 4, 5))
print(mimi)
