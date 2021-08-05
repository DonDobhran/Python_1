translate_dict = {"One": "Один",
                  "Two": "Два",
                  "Three": "Три",
                  "Four": "Четыре",
                  "Five": "Пять",
                  "Six": "Шесть",
                  "Seven": "Семь"}

with open('L5_T4_Dict.txt', encoding="utf-8") as file_read, open('L5_T4_Dict_1.txt', 'w', encoding='utf-8') as file_write:
    for line in file_read.readlines():
       text_number, number = line.rstrip().split(' - ')
       file_write.write(f'{translate_dict[text_number]} - {number}\n')
