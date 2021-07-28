input_string = input("введите строку из нескольких слов: ")
input_words = input_string.split()

for index, word in enumerate(input_words, 1):
    print(index+1, word[:10])