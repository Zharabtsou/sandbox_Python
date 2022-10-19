item_list = ['Honda', 'Volcvagen', 'Toeta', 'passat', 'mazda', 'Vaz', 'Gaz', 'BMW', 'Audi']
print(item_list)
#копируем список
copy_item_list = item_list[:]
print(copy_item_list)
print()
# добовляем разные окончание в конец списка
item_list.append('gelly')
copy_item_list.append('volvo')
# проверяем разные списки
print(item_list)
print(copy_item_list)
#перебераем список и выводим все элементы списка по отдельности
for item in item_list:
    print(f"My car: {item.title()}!")
print()

for item in copy_item_list:
    print(f"My car coppy: {item.title()}!")
print()