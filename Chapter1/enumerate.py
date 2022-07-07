word = "hello"

for index in range(len(word)):
    print(index)

for index, char in enumerate(word):
    print(index)

river = "Mississippi"
target = input('Input a character to find: ')
for index, letter in enumerate(river):
    if letter == target:
        print("letter found at index: ", index)
        break
else:
    print('letter', target, 'not found in', river )


s = "I love Python"

print(s.split())


print("I love Python".partition("y"))
