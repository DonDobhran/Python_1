Pribil = float(input("Введите прибыль фирмы"))
Zatraty = float(input("Затраты фирмы"))
Profit = Pribil-Zatraty

if Profit > 0:
    print(f"Рентабельность капитала {Profit/Pribil*100:2f}%")
    shtat = int(input("Укажите количество струдников"))
    print(f"Чистая прибыль на 1 сотрудника: {Profit/shtat}")
elif Profit < 0:
    print("Фирма не приносит прибыли")
else:
    print("у Компании нулевая прибыль")