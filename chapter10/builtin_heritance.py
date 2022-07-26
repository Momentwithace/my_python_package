class MyCustomList(list):

    def __getitem__(self, item):
        print("getting item")
        super().__getitem__(item)

    def __setitem__(self, key, value):
        if value < 1:
            print("Not adding it")
            return
        super().__setitem__(key, value)

    def append(self, value) -> None:
        if value < 1:
            print("Not adding it")
            return
        super().append(value)

    class AppException(Exception):
        def __init__(self, msg) -> None:
            super(self).__init__(msg)

    raise AppException("This exception is a example of how exceptions are made")


c = MyCustomList()
print(c)
c.append(2)
c.append(0)
print(c)
