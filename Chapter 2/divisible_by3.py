number = int(input("Enter a number: "))
result = number % 3
print("The reminder of " + str(number) + " is " + str(result))
if number % 2 == 0:
    print(str(number) + " is divisible by 3")
else:
    print(str(number) + " is not divisible by 3")
