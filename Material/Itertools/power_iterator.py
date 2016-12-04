class PowerNumbers:
    def __init__(self, a, n):
        self.a = a
        self.n = n

    def __iter__(self):
        return PowerNumberIterator(self.a, self.n)


class PowerNumberIterator:
    def __init__(self, a, n):
        self.a = a
        self.n = n
        self.current = 1
        self.i = 0
        print(self.a)

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            ret = self.current
            self.i += 1
            self.current = self.current * self.a
            return ret
        else:
            raise StopIteration


def get_powers(a, n):
    current = 1
    for _ in range(n):
        yield current
        current *= a
