#создаем с помощью range список чисел и выводим их
list_items = []
for item in range(1, 1_000_000):
    list_items.append(item)
    print(item)
print('THE END!')
