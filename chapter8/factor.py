number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if number % i == 0:
        print(f"{i} is a Factor of {number}")
