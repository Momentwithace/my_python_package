def histogram(word: str) -> dict[str, int]:
    import string
    abc = string.ascii_lowercase

    map_ = {}

    for char in abc:
        map_[char] = word.lower().count(char)
    return map_

def histogram_2(word):
    import string
    return {char: word.lower().count(char) for char in string.ascii_lowercase}

print(histogram("Ace alone"))
