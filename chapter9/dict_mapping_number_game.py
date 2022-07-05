numbers = input("Number: ")
numbers_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
output = ""
for number in numbers:
    # the ! would be displayed if the user enters a number that's not in our dict
    output += numbers_mapping.get(number, "!") + "  "
print(output)