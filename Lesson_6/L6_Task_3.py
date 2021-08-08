"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров).
"""


class Worker:
    _income_dict = {"Оклад": [7000, 10000, 15000, 30000], 'Премия': [3000, 5000, 10000, 15000]}

    def __init__(self, _name, _surname, _position):
        self._name = name
        self._surname = surname
        self._position = position


class Position(Worker):

    def get_full_name(self, _name, _surname):
        print(f'Трудоустроен {name} {surname}')

    def get_total_income(self, _input_wage, _input_bonus, _name):
        try:
            print(f'{name} назначен на должность - {position}, с суммарной ЗП - '
              f'{Worker._income_dict.get("Оклад")[input_wage-1] + Worker._income_dict.get("Премия")[input_bonus-1]} '
              f'руб.')
        except IndexError:
            print("Данные коды оклада и премиальной части не включены в табель")


name = input("Введите имя сотрудника: ")
surname = input("Введите фамилию сотрудника: ")
position = input("Введите должность сотрудника: ")
print(f'Табель окладов:')
for index, bonus in enumerate(Worker._income_dict.get("Оклад"), 0):
    print(index+1, bonus)
input_wage = int(input("Введите код оклада из указанного выше табеля: "))
print('Табель премий:')
for index, bonus in enumerate(Worker._income_dict.get("Премия"), 0):
    print(index+1, bonus)
input_bonus = int(input("Введите код премиальной части сотрудника из указанного выше табеля: "))

Worker_1 = Position(name, surname, position)
Worker_1.get_full_name(name, surname)
Worker_1.get_total_income(input_wage, input_bonus, name)


# Подсчёт суммарной ЗП из библиотеки, что б не забыть.
# income_dict = {"Оклад": [7000, 10000, 15000, 30000], 'Премия': [3000, 5000, 10000, 15000]}
# i = 0
# for sum_salary in range(i, len(income_dict.get("Оклад"))):
#     print(income_dict.get("Оклад")[i] + income_dict.get("Премия")[i])
#     i += 1


