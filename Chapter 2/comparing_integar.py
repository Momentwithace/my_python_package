num = int(input("Enter a number: "))
num1 = 100

square_of_num = num * num

print("Square of the number is: " + str(square_of_num))

if square_of_num > num1:
    print("Square of number " + str(square_of_num) + " > " + str(num1))
if square_of_num < num1:
    print("Square of number " + str(square_of_num) + " < " + str(num1))
if square_of_num == num1:
    print("Square of number " + str(square_of_num) + " == " + str(num1))
if square_of_num != num1:
    print("Square of number " + str(square_of_num) + " != " + str(num1))
