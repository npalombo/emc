__author__ = 'nick'


class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, arg):
        if arg not in self.memo:
            self.memo[arg] = self.fn(arg)
        return self.memo[arg]


@Memoize
def fib(n):
    if n > 0:
        a, b = 0, 1
        seq = [a]
        for i in range(n - 1):
            a, b = b, a + b
            seq.append(a)
        return seq
    else:
        raise Exception('Argument must be at least 1')