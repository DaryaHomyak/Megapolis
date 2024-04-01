# python
import csv


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


# алгоритм для сортировки за n*log(n)
def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p - 1)
    quick_sort(array, p + 1, end)


data = []
data1 = []
new_data = []
res = []
# открытие файла
with open("transactions.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    for i in range(1, len(data)):
        item = data[i].split("?")
        res.append([item[0], item[1], item[2], item[3], item[4], float(item[5].replace(",", ".")), item[6]])
    data = []
    # Сортировка по названию
    for i in res:
        data.append(i)
        data1.append(i[4])
    quick_sort(data1, 0, len(data1) - 1)
    for i in data1:
        for j in range(len(data)):
            if data[j][4] == i:
                new_data.append(data[j])
    count = 1
    # топ-5 элементов
    for el in new_data:
        print(f'{el[1]} - {el[4]} - {el[6]}')
        count += 1
        if count == 5:
            break
