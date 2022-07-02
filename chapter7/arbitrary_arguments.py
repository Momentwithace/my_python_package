def add(*args):
    return sum(args)

print(add(1, 2, 3, 4, 5))

def avg(*numbers):
    return sum(numbers) / len(numbers)

print(avg(1, 2, 3, 4))
print(avg(1, 2, 3))

lst = [1, 2, 3, 4, 5]
# the star symbol shows that in other for a arbitrary to work on a list we need to unpack it using the star symbol
print(avg(*lst))

set_ = {1, 2, 3, 4, 5}
print(avg(*set_))