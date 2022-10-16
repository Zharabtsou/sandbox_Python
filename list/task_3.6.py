#Удаляем людей из списка пока там не останится n людей, а в конце очистим список 2-мя методами.

guest_name = ['Andrey']
name = ''

#запрашиваем имя гостей наполняем список
while name != 'end':
    name = input('введите имя гостя : ')
    guest_name.append(name)

#перебираем список гостей и выводим в консоль
for guest_list in guest_name:
    if guest_list == 'end':
        break
    else:
        print(f'Уважаймый {guest_list.title()} приглашаем вас к нам на мероприятие')
del guest_name[-1] #удаляем слово end в списке -1 это зачит последнее слово в конце списка


print(guest_name)

# remove удаление элемента из списка по значению
guest_name.remove('Andrey')
print(guest_name)
