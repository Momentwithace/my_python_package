# iterators

hello = iter("hello")
print(next(hello))
print(next(hello))
print(next(hello))
print(next(hello))
print(next(hello))

messages = iter(["hello", "how", "are", "you"])
print(next(messages))
print(next(messages))
print(next(messages))
print(list(messages))


