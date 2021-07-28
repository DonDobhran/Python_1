my_rating_list = [10, 8, 6, 4, 3, 1]
my_rating_list_copy = my_rating_list.copy()

new_rating = int(input("Введите новый элемент рейтинга: "))

try:
    if new_rating > my_rating_list[0]:
        my_rating_list_copy.insert(0, new_rating)
    elif new_rating < my_rating_list[-1]:
        my_rating_list_copy.append(new_rating)
    else:
        for rating in my_rating_list:
            if new_rating == rating:
                rating_index = my_rating_list.index(rating)
                rating_count = my_rating_list.count(rating)
                new_rang_index = rating_index + rating_count
                my_rating_list_copy.insert(new_rang_index, new_rating)
                break
            elif new_rating > rating:
                my_rating_list_copy.insert(my_rating_list.index(rating), new_rating)
                break
            else:
                continue

except IndexError:
     print("Неверне входные данные...")

print(my_rating_list_copy)
