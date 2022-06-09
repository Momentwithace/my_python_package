def summing_digit(n):
    sum = 0
    while n > 0:
        divider = n % 10
        sum += divider
        n = n // 10
    return sum


number = int(input("Enter five integer number: "))
result = summing_digit(number)
print("Sum of digit is :" + str(result))
