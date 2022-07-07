number = int(input("Enter a number: "))
num_sqr = number * number
if len(str(num_sqr - 1)) == number or len(str(num_sqr - 2)) == number:
    print("Number is An Anagram")
else:
    print("Number Isn't An Anagram")




