res = []
with open("transactions.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    # достанем данные из файла
    for i in range(1, len(data)):
        item = data[i].split("?")
        res.append([item[0], item[1], item[2], item[3], item[4], float(item[5].replace(",", ".")), item[6]])
    # ввод пользователем кода товара
    item_code = input()
    # поиск по списку товаров
    while item_code != "none":
        is_finded = False
        for i in res:
            # если элемент нашёлся
            if i[3] == item_code:
                print(f"По вашему запросу: {item_code} найден следующий вариант:")
                print(*i)
                is_finded = True
        # если элемент не будет найден
        if not is_finded:
            print("Такого товара в базе нет")
        # новый ввод пользователем кода товара
        item_code = input()
