class LCG:

    def __init__(self, seed, multiplier, increment, modulus):
        if multiplier <= 0 or modulus <= multiplier:
            raise ValueError("Error: multiplier must follow '0 < a < M'")
        if increment < 0 or increment >= modulus:
            raise ValueError("Error: increment must follow '0<= c < M'")
        self._seed = seed
        self._multiplier = multiplier
        self._increment = increment
        self._modulus = modulus

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, val):
        self._seed = val

    def __iter__(self):
        return self

    def __next__(self):
        return self._generate_()

    def _generate_(self):
        ''' Generates the next value using LCG. '''
        self.seed = (self._multiplier * self.seed +
                     self._increment) % self._modulus
        return self.seed

    def next(self, n):
        ''' Returns a list of the next n random numbers '''
        return [self._generate_() for i in range(0, n)]


class SCG(LCG):

    def __init__(self, seed, multiplier, increment, modulus):
        if seed % 4 != 2:
            ValueError("seed must follow 'X mod 4 = 2'")
        super().__init__(seed, multiplier, increment, modulus)

    def _generate_(self):
        ''' Generates the next value using SCG. '''
        self._seed = (self.seed * (self.seed + 1)) % self._modulus
        return self._seed


if __name__ == '__main__':

    # Create LCG generator
    rand1 = LCG(1, 1103515245, 12345, 2 ** 32)
    print(rand1.__next__())
    # 1103527590

    print(rand1.next(10))
    # [2524885223, 662824084, 3295386429, 4182499122, 2516284547, 3655513600, 2633739833, 3210001534, 267834847, 180171308]

    # Create SCG generator
    rand2 = SCG(1, 1103515245, 12345, 2 ** 32)
    print(rand2.next(10))
    # [2, 6, 42, 1806, 3263442, 2833024022, 3537057274, 5287454, 1232959906, 2944140326]

    # Use iterator to get random numbers
    it = iter(rand2)
    count = 0
    for val in it:
        if count > 10:
            break
        print(val)
        count += 1
    # 2824681930
    # 3526151470
    # 1987019122
    # 280991798
    # 1272169370
    # 2367929406
    # 3699563330
    # 3075790918
    # 1878723434
    # 3193525070
    # 2377187090
