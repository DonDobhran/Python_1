def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    return sum(my_list[:2])


print(my_func(10, 8, 12))