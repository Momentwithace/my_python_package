number = int(input("Enter Any Number: "))
number_square = str(number * number)
length = len(number_square)
if str(number) == number_square[-1:] or str(number) == number_square[-2:]:
    print("Number is Anagram")
else:
    print("Number Isn't An Anagram")