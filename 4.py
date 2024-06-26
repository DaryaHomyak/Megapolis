import csv

res = []
with open("transactions.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    # достанем данные из файла
    for i in range(1, len(data)):
        item = data[i].split("?")
        res.append([item[0], item[1], item[2], item[3], item[4], item[5], float(item[6].replace(",", "."))])
        users_purshase = {}
        for i in res:
            if i[0] not in users_purshase:
                users_purshase[i[0]] = {'summ': 0}
                users_purshase[i[0]]['summ'] += int(i[5]) * i[6]

            else:
                users_purshase[i[0]]['summ'] += int(i[5]) * i[6]
    # Отсортируем по цене
    users_purshase = sorted(users_purshase.items(), key=lambda item: item[1]['summ'])
    data = []
    for i in range(-1, -8, -1):
        data.append([users_purshase[i][0], users_purshase[i][1]['summ']])
print(data)
# запишем в файл:
with open('best_buyer.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerows(data)
