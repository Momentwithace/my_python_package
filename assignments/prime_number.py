# lst = [i for i in range(1, 11)]
# print(lst)
#
# lst = [i ** 2 for i in range(1, 11)]
# print(lst)
#
# lst = [i ** 2 for i in range(1, 11) if i % 2 == 0]
# print(lst)
#
# lst = ["even" if 3 % 2 == 0 else "odd"]
# print(lst)
#
# lst = [i ** 2 if i % 2 == 0 else i for i in range(1, 11)]
# print(lst)
#
# lst = [int(input(f"Enter Student {i}'s score:  ")) for i in range(1, 6)]
# print("Sum is: =", sum(lst))
# print("Maximum is: =", max(lst))
# print("Minimum is: =", min(lst))
#
#
# def is_prime(num: int) -> bool:
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#
#     return True
#
#
# print(is_prime(12))


# def is_prime(num: int) -> bool:
#     max_divisor = (num // 2 + 1)
#     for i in range(2, max_divisor):
#         if num % i == 0:
#             return False
#
#     return True
#
#
# Number = (int(input("Enter Number:")))
# print(is_prime(Number))


# def cube(num: int) -> int:
#     return num ** 3
#
#
# cube = [cube(i) for i in range(1, 11)]
# print(cube)
# import math
#
# def is_prime(num: int) -> bool:
#     max_divisor = math.ceil(math.sqrt(num)) + 1
#     for i in range(2, max_divisor):
#         if num % i == 0:
#             return False
#
#     return True

# prime = int(input("Enter a number -> "))
# print(is_prime(prime))
#
# primes = (i for i in range(1, 10_000_000) if is_prime(i))
# print(type(primes))
#
# primes = {k: v for k, v in enumerate(range(1, 10)) if is_prime(v)}
# print(type(primes))
# print(primes)

