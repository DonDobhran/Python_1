def division():
    try:
        a = float(input("Введите число А: "))
        b = float(input("Введите число B: "))
        divide = a/b
        return divide
    except ZeroDivisionError:
        return "Делить на ноль нельзя!"
    except ValueError:
        return "Необходимо чтобы введённые данные были числами"


print(division())
