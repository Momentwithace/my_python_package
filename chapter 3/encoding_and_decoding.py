import string

word = str(input("Enter a word to encode: "))

while not word.isalpha():
    print("Enter an alphabetical word to encode ")
    word = input("Enter a word to encode: ")

key = (input("Enter a key between 1 - 26: "))

while not key.isdigit() or not 1 < int(key) <= 26:
    print("Enter a digit between 1 - 26 to set your key")
    key = input("Enter a key between 1 - 26: ")

print(key)
if word.isalpha() and key.isdigit():
    key = int(key)
    abc = string.ascii_lowercase
    trans_abc = abc[key: ] + abc[ :key]
    encoded_word = word.translate(str.maketrans(abc, trans_abc))
    print("encoded_word is " + encoded_word)

    result = int(input("Enter 1 to decode: "))

    if result == 1:
        print(encoded_word.translate(str.maketrans(trans_abc, abc)))

else:
    print("This is an Encrypted message")
