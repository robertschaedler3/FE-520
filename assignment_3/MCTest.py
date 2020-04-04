import time
import numpy as np
import math

from generator import LCG, SCG
from point import Point


def test(gen, num_points=10000000):
    ''' Tests a generator by estimating the ratio of points that fall within a circle. '''
    start = time.time()
    it = iter(gen)
    points = np.fromiter(it, float, count=num_points)
    points = 2 * ((points - min(points)) / (max(points) - min(points))) - 1

    circle_count = 0
    for i in range(0, num_points):
        p = Point(points[i], points[i])
        circle_count += 1 if p.distance() <= 1 else 0

    end = time.time()

    print(f'\nTested {num_points} points in {(end - start):.5f} seconds.')
    print(f'Result: {(math.pi/4 - circle_count/num_points):.5f}\n')


if __name__ == '__main__':
    lcg = LCG(1, 1103515245, 12345, 2 ** 32)
    scg = SCG(1, 1103515245, 12345, 2 ** 32)

    test(lcg)
    # Tested 10000000 points in 53.30481 seconds.
    # Result: 0.07810

    test(scg)
    # Tested 10000000 points in 38.56882 seconds.
    # Result: 0.07843
