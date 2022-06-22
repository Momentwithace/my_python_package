import string


def encoder(message: str, key: int ) -> str:
    abc = string.ascii_lowercase
    key = 5
    transform = abc[key:] + abc[:key]
    encrypted_word = message.translate(str.maketrans(abc, transform))
    return encrypted_word

word = encoder('hello', 4)

print(word)


def decoder(message: str, key: int) -> str:
    abc = string.ascii_lowercase
    key = 5
    transform = abc[key:] + abc[:key]
    decrypted_word = message.translate(str.maketrans(transform, abc))
    return decrypted_word

word = decoder('mjqqt', 4)

print(word)
