result_1day = int(input("Результат спортсмена в первый день: "))
gelanie = int(input("Желаемая дистанция"))
days = 1
while result_1day < gelanie:
    result_1day *= 1.1
    days += 1

print(f"Спортсмен достигнет дистанции в {gelanie} км за {days} дней")