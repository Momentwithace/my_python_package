def add(a, b):
    return a + b


addition = add
print(addition(2, 3))


def operator(a, b, func):
    return func(a, b)


print(operator(3, 6, add))


def plus(a):
    def func(b):
        return a + b

    return func

add_5 = plus(5)
print(add_5(7))