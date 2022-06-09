number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

triple_of_number1 = number1 * number1 * number1
double_of_number2 = number2 * number2

if triple_of_number1 % double_of_number2 == 0:
    print("True")
else:
    print("False")