import math
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sqr_of_num1 = num1 * num1
print("Square of num1 is: " + str(sqr_of_num1))
sqr_of_num2 = num2 * num2
print("Square of num2 is: " + str(sqr_of_num2))

sum_of_both_square = sqr_of_num1 + sqr_of_num2

print("Sum of both square is: " + str(sum_of_both_square))

diff_of_both_square = sqr_of_num1 - sqr_of_num2

print("Diff of both square is {:3d}".format(diff_of_both_square))



