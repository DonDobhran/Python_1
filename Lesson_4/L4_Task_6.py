from itertools import count, cycle
import sys

start_from = 10
iterable = "ABCDEF"
iterations_count = 0

def integrator_generator(start_from):
    for el in count(start_from):
        if el > start_from+10:
            break
        yield el


# for el in integrator_generator(15):
#     print(el)

# gen = integrator_generator(10)
# print(sys.getsizeof(gen))
# print(sys.getsizeof(list(gen)))

for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 3:
        print(el)
    else:
        break