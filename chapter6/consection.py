from functools import reduce


def num_sum(a: int, b: int):
    """adds two numbers"""

    return a + b


# def subtract(m, n):
#     return m - n


def operate(fn, x, y):
    return fn(x, y)


def subtract_(m, n):
    return m - n


print(operate(subtract_, 5, 2))

print(operate(lambda x, y: x * y, 3, 4))

division = lambda p, q: p / q
print(division(3, 5))

print(division.__name__)

list_of_string = "i love chukwuemeka".split()

print(max(list_of_string, key=len))

print(max(list_of_string, key=lambda x: x[-1]))

# this example above is an higher order function
# a function that either return,
# takes it in or deals with it in short

ages = [{"name": "ade", "age": 8}, {"name": "titi", "age": 16}]
ages = [{"name": "Adebayo", "age": 8}, {"name": "titi", "age": 16}]

print(max(ages, key=lambda x: x["name"]))
print(max(ages, key=lambda x: len(x["name"])))
print(sorted(ages, key=lambda x: len(x["name"])))
print(sorted(ages, key=lambda x: x["name"]))

print(operate(num_sum, 2, 3))

print(num_sum(2, 3))

print(num_sum.__name__)

print(num_sum.__doc__)

print(num_sum.__annotations__)

lst = [2, 3, 4, 5]
sqr = [4, 9, 16, 25]

# getting the square of the numbers in a list using lambda

print(list(map(lambda x: x ** 2, [2, 3, 4, 5])))

print(list(filter(lambda x: x > 2, lst)))

print(sum([1, 2, 3, 4, 5], 10))

print(reduce(lambda x, y: x + y[1, 2, 3, 4], 5))
