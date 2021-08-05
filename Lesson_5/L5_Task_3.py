sum = 0


with open('L3_T3_Salary.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        surname, salary = line.split()
        sum += int(salary)
        if int(salary) < 20000:
            print(f"Менее 20 тыс.руб. оклад у {surname}")


print(f"Средняя величина дохода сотрудника: {sum/len(lines)}")