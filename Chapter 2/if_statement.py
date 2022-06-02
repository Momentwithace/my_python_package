print("Enter two number and i will tell you \
the relationship they have")
first_number = int(input("enter first number :"))
second_number = int(input("enter second number :"))
print('ready')
if first_number == second_number:
    print(first_number, 'is equal to', second_number)

if first_number != second_number:
    print(first_number, 'is not equal to', second_number)

if first_number < second_number:
    print(first_number, 'is lesser than ', second_number)

if first_number > second_number:
    print(first_number, 'is greater than ', second_number)

if first_number <= second_number:
    print(first_number, 'is less than or equal to ', second_number)

if first_number >= second_number:
    print(first_number, 'is greater than or equal to ', second_number)