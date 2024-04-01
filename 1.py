# python
# Импортируем библиотеку для работы с csv файлами
import csv
res = []
cheapest = ["", 999999999999]
with open("transactions.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    for i in range(len(data)):
        item = data[i].split("?")
        if "набор" in item[4].lower():
            res.append([item[4], float(item[-2].replace(",", "."))])
            if float(item[-2].replace(",", ".")) < cheapest[1]:
                cheapest = [item[4], float(item[-2].replace(",", "."))]
with open('pack.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerows(res)
with open("cheap_product.txt", "w",  encoding='utf-8') as f:
    f.write(f'Самый дешевый товар в категории набор: {cheapest[0]}, цена такого товара составит: {cheapest[1]}')
    print(f'Самый дешевый товар в категории набор: {cheapest[0]}, цена такого товара составит: {cheapest[1]}')