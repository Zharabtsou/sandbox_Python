#создаем с помощью range список чисел и выводим их находим максимум минимкм и сумму
list_items = []

for item in range(1, 1_000_001): #если мы хотим число от 1 до 1_000_000 то нужно писать 1_000_001!!!
    list_items.append(item)



print('THE END!')
print(max(list_items)) #находим максимум из списка
print(min(list_items)) #находим минимкм из списка
print(sum(list_items)) #находим сумму списка