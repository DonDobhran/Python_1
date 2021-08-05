import json

result_list = []
dict_plus_profit = {}
dict_min_profit = {}
with open('L5_T7_Database.txt', encoding="utf-8") as file:
    average_profit_list = []
    for line in file.readlines():
        name, _, revenue, costs = line.rstrip().split()
        profit = int(revenue) - int(costs)
        if profit > 0:
            average_profit_list.append(profit)
            dict_plus_profit.update({name:profit})
        else:
            dict_min_profit.update({name:profit})
    result_list.append(dict_plus_profit)
    result_list.append(dict_min_profit)
    result_list.append({"average_profit": sum(average_profit_list)/len(average_profit_list)})

with open("File7.json", "w", encoding="utf-8") as file:
    json.dump(result_list, file, ensure_ascii=False, indent="")