# def generator():
#     start = 1
#     while True:
#         yield start
#         start += 1
#
#
# gen = generator()
#
# print(next(gen))
# print(next(gen))


def generator(num):
    start = 1
    while start != num:
        yield start
        start += 1
        yield "poof"


gen = generator(10)

print(next(gen))
print(next(gen))
print(next(gen))

print(list(gen))
