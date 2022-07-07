def max_min(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num3:
        return num2
    else:
        return num3


print(max_min(7, 9, 19))
number = min(2, 3, 4)
print(number)

number = max(45, 76, 89, 54)
print(number)