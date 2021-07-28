def sum_calc(input_string):
    input_list = input_string.split()
    my_sum = 0
    for el in input_list:
        if el:
            try:
                if el == "N":
                    return my_sum, False
                else:
                    my_sum += float(el)
            except ValueError:
                continue
    return my_sum, True


continue_flag = True
result_sum = 0
while continue_flag:
    input_string = input("Введите числа через пробел. Для остановки введите символ N: ")
    current_sum, continue_flag = sum_calc(input_string)
    result_sum += current_sum
    print("Промежуточная сумма: ", result_sum)
print("Результирующая сумма: ", result_sum)