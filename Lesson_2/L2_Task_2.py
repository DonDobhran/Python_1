input_list = input("Введите элементы списка через пробел: ")
input_list = input_list.split()

for index in range(0, len(input_list)-1, 2):
    input_list[index], input_list[index+1] = input_list[index+1], input_list[index]

print(input_list)