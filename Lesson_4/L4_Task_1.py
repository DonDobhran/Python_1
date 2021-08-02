
from sys import argv


script_name, productivity, rate_per_hour, bonus = argv
# script_name, productivity, rate_per_hour, bonus = argv
print("Имя скрипта ", script_name)
print("Выработка в часах ", productivity)
print("Ставка одного часа ", rate_per_hour)
print("Бонус", bonus)
print("Зарплата ", int(productivity) * int(rate_per_hour) * int(bonus))