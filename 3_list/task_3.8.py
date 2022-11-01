#простой список стран
list_countri = ["США", "Япония", "Канада", "Польша", "Чехия"]
#выводим список стран без сортировки
print(list_countri)
#сортируем список стран но только на время вывода в консоль
print(sorted(list_countri))
#проверяем что список не был изменен. тоеть не отсортирован
print(list_countri)
#сортируем список стран и выводим его в обратном порядке
print(sorted(list_countri, reverse=True))
#проверяем что список не был изменен.
print(list_countri)
#переворачиваем список
list_countri.reverse()
#проверяем изменение
print(list_countri)
#переворачиваем список
list_countri.reverse()
#проверяем изменение
print(list_countri)
#сортируем список и сохраняем изменение сортировки
list_countri.sort()
#проверяем изменение
print(list_countri)
#сортируем список и сохраняем изменение сортировки
list_countri.sort(reverse=True)
#проверяем изменение
print(list_countri)
#выводим блину списка. Количесво элементов в списке
print(len(list_countri))