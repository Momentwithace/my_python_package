class Counter:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            result = self.start
            self.start += self.stop
            return result
        else:
            raise StopIteration


counter = Counter(1, 5)

for count in counter:
    print(count)
