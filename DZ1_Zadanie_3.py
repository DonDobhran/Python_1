"""""
Сложение введённого числа в двойное и тройное
"""""
try:
    n = input("Введите простое число от 0 до 9 ")
    nn = n + n
    nnn = n+n+n
    summa_n = int(n)+int(nn)+int(nnn)
    print(summa_n)

except Exception: print("Вы ввели некорректные данные, необходимо число от 0 до 9")
