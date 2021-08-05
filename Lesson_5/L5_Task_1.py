input_str = input("Введите строку: ")
with open("File.txt", "w") as file:
    while input_str:
        file.write(input_str+'\n')
        input_str = input("Введите следующую строку")