my_list_structure = [
    (1, {"Название": "компьютер", "Цена": 20000, "количество": 5, "ед": "шт"}),
    (2, {"Название": "принтер", "Цена": 6000, "количество": 2, "ед": "шт."}),
    (3, {"Название": "сканер", "Цена": 2000, "количество": 7, "ед": "упак."})
]

my_result_dict = {}

for structure in my_list_structure:
    structure_number, structure_info_dict = structure
    for key, value in structure_info_dict.items():
        value_list = my_result_dict.get(key, [])
        if value not in value_list:
            value_list.append(value)
        my_result_dict[key] = value_list

print(my_result_dict)