from datetime import datetime
import time


def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(datetime.now())
        print("About to be decorated")
        value = func(*args, **kwargs)
        # func()
        print(datetime.now())
        print("Just decorated")
        return value

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        time_taken = time.perf_counter() - start
        print(f"{func.__name__} took {time_taken} secs to load")

        return val

    return wrapper


@print_decorator
def printer():
    print("I am a printer")


printer()

ace = print_decorator(printer)

@print_decorator
@timer
def factorial(num: int) -> int:
    import math
    return math.factorial(num)

print(factorial(8))
