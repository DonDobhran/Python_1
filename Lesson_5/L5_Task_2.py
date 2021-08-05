with open('File.txt', 'r') as f_obj:
    content = f_obj.readlines()
    print(content)
    print(f"Количество строк в файле: {len(content)}")
    for i in range(0, len(content)):
        print(len(content[i].split()))
        print(f"Кол-во слов в строке  {i+1} равно {len(content[i].split())}")
        