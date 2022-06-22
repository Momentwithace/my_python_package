def fibonacci(n):
    a, b = 0, 1
    count = 0
    if n < 0:
        print('Incorrect Input')
    elif n == 1:
        print(a)
    else:
        while count < n:
            print(a, end=" ")
            number = a + b
            a = b
            b = number
            count += 1



fibonacci(9)