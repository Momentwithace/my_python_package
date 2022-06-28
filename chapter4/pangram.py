import string


def pangram(sentence):
    return set(string.ascii_lowercase) <= set(sentence.lower())


result = pangram("i love you")

print(result)


def is_pangram(s):
    s = s.lower()
    return all(letter in s for letter in string.ascii_lowercase)

result = is_pangram("please don't touch my laptop")

print(result)