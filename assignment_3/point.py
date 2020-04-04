import math


class Point:

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def distance(self):
        ''' Computes the distance between a point and the origin. '''
        return math.sqrt(self.__x ** 2 + self.__y ** 2)
