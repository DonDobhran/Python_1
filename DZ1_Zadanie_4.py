input_number = input("Введите целое число больше нуля ")
number_length = len(input_number)
i = 0
max_element = 0
while i < number_length:
    element = int(input_number[i])
    if element > max_element:
        max_element = element
        i += 1
print(max_element)