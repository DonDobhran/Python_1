result_dict = {}
with open('L5_T6_Dict.txt', encoding='utf-8') as file:
    for line in file:
        lesson_type, *lessons = line.split(': ')
        lesson_count = [int(lesson.rstrip('(л)(пр)(лаб)')) for lesson in lessons if lesson != '-']
        result_dict.update({lesson_type.rstrip(':'): sum(lesson_count)})

print(result_dict)