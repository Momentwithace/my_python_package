class Rectangle:
    def __int__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):

    def __int__(self, side_length):
        self.side_length = side_length


a = Square()
a.area()