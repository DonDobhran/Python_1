my_func_pow = lambda x, y: x**y

def my_func(x: int, y: int) -> float:
    if y > 0:
        return
    elif y == 0:
        return 1
    elif x <= 0:
        return
    else:

        x_pow_y = 1
        while y < 0:
            x_pow_y *=1/x
            y += 1
        return x_pow_y


# result = my_func_pow(2, -3)
result = my_func(2, -3)
print(result if result else "Неверные входные данные")