my_struct = []
while True:
    check_inputs = input("Продолжить список? (y/n): ")
    if check_inputs == 'y':
        my_dict = dict({'Название': input("Введите название товара: "), 'Цена': input("Введите цену товара: "),
                        'Количество': int(input("Введите количество товара: ")), 'ед': input('Введите единицу '
                                                                                             'измерения: ')})
        my_struct.append((len(my_struct)+1, my_dict))
    elif check_inputs == 'n':
        break
    else:
        check_inputs = input("Продолжить список? (y/n): ")
print(my_struct)