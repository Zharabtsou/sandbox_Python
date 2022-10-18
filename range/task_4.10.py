item_list = ['Honda', 'Volcvagen', 'Toeta', 'passat', 'mazda', 'Vaz', 'Gaz', 'BMW', 'Audi']
#выводим срез списка и не забываем если нужно ввывести 3 элемента то это 0 1 2 а элемен под номерам 3 это конец
print(f'мой список машин {item_list[0:3]}')
print()
#выводим элементы с 0 оп 2 включительно тоесть +1
for item in item_list[0:3]:
    print(f'мой список машин {item}')
print()
#выводим с середины списка
for item in item_list[2:5]:
    print(f'мой список машин {item}')
print()

#выводим с середины списка
# -3 это значит третий с конца и до конца списка
for item in item_list[-3:]:
    print(f'мой список машин {item}')