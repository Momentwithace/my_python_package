def duplicate_encode(word):
    lower_case = word.lower()

    letters = [i for i in word]

    for i in range(len(letters)):
        count = letters.count(letters[i])

        if count > 1:
            letters[i] = ")"

        else:
            letters[i] = "("

    return "".join(letters)


print(duplicate_encode("success"))
