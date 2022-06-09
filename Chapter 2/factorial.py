def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1


number = int(input("Enter a number: "))
result = factorial(number)
print("Factorial is :" + str(result))
