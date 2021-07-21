"""""
Сколько времени в формате чч:мм:сс в ведённом числе в секундах
"""""

try:
    Seconds_input = int(input("Укажите время в секундах:"))
    hour = Seconds_input // 3600
    Minutes = Seconds_input % 3600 // 60
    seconds = Seconds_input % 3600 % 60
    print(f"{hour:02d}:{Minutes:02d}:{seconds:02d}")

except Exception:
    print("Следует указать числовое значение в секундах")
