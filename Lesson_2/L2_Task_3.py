try:
    number_of_month = int(input('Введите номер месяца числом от 1 до 12: '))
except ValueError:
    print("Неверно введён номер месяца")
else:

    seasons_dict = {}
    seasons_dict = seasons_dict.fromkeys([12, 1, 2], 'Зима')
    seasons_dict.update({}.fromkeys([3, 4, 5], 'Весна'))
    seasons_dict.update({}.fromkeys([6, 7, 8], 'Лето'))
    seasons_dict.update({}.fromkeys([9, 10, 11], 'Осень'))

    for season_month_number, season in seasons_dict.items():
        if number_of_month == season_month_number:
            print(season)
            break
    else:
        print('Время года не определено')