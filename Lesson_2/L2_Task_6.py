my_struct = []
count = 0
while True:
    try:
        check_inputs = input("Продолжить список? (y/n): ")
        if check_inputs == 'y':
            my_dict = dict({'Название': input("Введите название товара: "), 'Цена': float(input("Введите цену товара: ")),
                            'Количество': int(input("Введите количество товара: ")), 'ед': input('Введите единицу '
                                                                                                 'измерения: ')})
            my_struct.append((len(my_struct)+1, my_dict))
            count = count + 1
        elif check_inputs == 'n':
            break
        else:
            check_inputs = input("Продолжить список? (y/n): ")
    except ValueError:
        print("В строке количество товара или цена указаны не числовые значения, необходимо повторить ввод списка")


print("По результатам ввода сформирован следующий список:")
i = 0
while i < count:
    print(f"Список № {i+1}: {my_struct[i]}")
    i = i + 1

my_result_dict = {}

for structure in my_struct:
    structure_number, structure_info_dict = structure
    for key, value in structure_info_dict.items():
        value_list = my_result_dict.get(key, [])
        if value not in value_list:
            value_list.append(value)
        my_result_dict[key] = value_list
print("")
print("База данных содержит:")
print(f"Категорию Название - {my_result_dict.get('Название')}")
print(f"Категорию Цена - {my_result_dict.get('Цена')}")
print(f"Категорию единиц измерения - {my_result_dict.get('ед')}")

# Неудавшаяся попытка вывести в предложения полученную базу... Выдаёт ошибку что я пытаюсь сравнить список с
# числовыми значениям "TypeError: list indices must be integers or slices, not str"

# print()
# print("В этой базе")
# i_dict = 0
# while i_dict < count:
# print("{Название[i_dict]} имеет цену - {Цена[i_dict]}, количество на складе: {Количество} {ед}".format(**my_result_dict))
# i_dict = i_dict + 1

