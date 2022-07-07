for number in range(1, 101):
    if not number % 15:
        print("fizzbuzz")
    elif not number % 3:
        print("buzz")
    elif not number % 5:
        print("fizz")
    else:
        print(number)