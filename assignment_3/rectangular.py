import numpy as np


class Rectangular:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


if __name__ == '__main__':
    r1 = Rectangular(10, 5)

    length = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    width = np.array([1, 100, 13, 4, 6, 7, 3, 1, 25, 7])
    r2 = Rectangular(length, width)

    print(r1.area())
    # 50
    print(r1.perimeter())
    # 30

    print(r2.area())
    # [  1 200  39  16  30  42  21   8 225  70]
    print(r2.perimeter())
    # [  4 204  32  16  22  26  20  18  68  34]
