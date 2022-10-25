item_list = ['Honda', 'Volcvagen', 'Toeta', 'passat', 'mazda', 'Vaz', 'Gaz', 'BMW', 'Audi']

#перебирает элементы в списке и если там есть элемент то печатает что такой элемент есть в списке.
if 'audi' in item_list:
    print('В списке есть Audi')
else:
    print('Такого элемента нету в списке')

#AND если в списке есть ОБА (ДВА) элеменра то правда иначе нет
if 'BMD' and 'Audi' in item_list:
    print('true')
else:
    print('Таких элементов нету в списке')

#OR если хотябы один элемент есть в списке то правда.
if 'BMD' or 'авакадо' in item_list:
    print('true')
else:
    print('Таких элементов нету в списке')

#NOT
if 'lada' not in item_list:
    print('Lada нет в списке')
else:
    print('Lada есть в списке')

#немного помиксуем элемент or and not
if (('BMW' and 'Audi') and ('BMD' or 'zaz')) and 'Lada' not in item_list:
    print('все условие соблюдены')
else:
    print('одно из условий не соблюдаецца')
