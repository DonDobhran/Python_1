from functools import reduce
from itertools import count


def fact(n):
    for i in count(1):
        if i <= n:
            result = reduce(lambda x, y: x*y range(1, i+1))
            yield result
        else:
            break

for el in fact(10):
    print(el)