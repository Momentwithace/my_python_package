def add(**kwargs):
    for k, v in kwargs.items():
        print(k, "==>", v)


add(b=6, c=5, a=7)

def add(a, *args, b=0, **kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)

add(5, 6, 7, 8, b=9, c=0, f=8, y=4)
