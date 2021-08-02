from functools import reduce

source_list = [el for el in range(1, 1001) if el % 2 == 0]

result = reduce(lambda x, y: x+y, source_list)
print(result)