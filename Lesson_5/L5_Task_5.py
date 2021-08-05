with open('File5.txt', 'w', encoding='utf-8') as file_w:
    input_numbers = input("Введите числа через пробел: ")
    print(input_numbers, file=file_w)

with open('File5.txt', encoding='utf-8') as file:
    content_list = file.read().rstrip().split()
    numbers_list = [int(number) for number in content_list if number.isdigit()]
    print(sum(numbers_list))