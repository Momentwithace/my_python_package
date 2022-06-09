num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum = num1 + num2 + num3
print("Sum is: " + str(sum))

average = sum / 3
print("average is :" + str(average))

product = num1 * num2 * num3
print("product is : " + str(product))

if num1 < num2 and num1 < num3:
    print(str(num1) + " is the smallest")
if num2 < num3 and num2 < num1:
    print(str(num2) + " is the smallest")
if num3 < num2 and num3 < num1:
    print(str(num3) + " is the smallest")

if num1 > num2 and num1 > num3:
    print(str(num1) + " is the largest")
if num2 > num3 and num2 > num1:
    print(str(num2) + " is the largest")
if num3 > num2 and num3 > num1:
    print(str(num3) + " is the largest")

