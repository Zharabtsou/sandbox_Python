list_people = { }
init_list_people = { }
info = input('для начала работы введите start: ')
while info != 'no':
    name = input('введите имя: ').title()
    age = int(input('Введите возврас: '))
    city = input('введите город: ').title()
    list_people[name] = {'age': age, 'citi': city }
    info = input('информация сохранена продолжаем?  ')

print('выводим информацию по всем пользователям котое были введены')
for key,info in list_people.items():
    print(f'\n{key}: ')
    for key,item in info.items():
        print(f'\t{key}: {item}')

info = input('иницилизирум весь список пользователей y/n: ')
if info == 'y':
    while list_people:
        name, info = list_people.popitem()
        init_list_people[name] = info
    print('Приступаем к инициализации словаря')
    for key, info in init_list_people.items():
        print(f'\n{key}: ')
        for key, item in info.items():
            print(f'\t{key}: {item}')
    print('словарь успешно проинициализирлванн')
else:
    print('!!!!!список остался не принилицирозированным!!!!!')
    print(f'не проиницилизированный список{list_people}')
    print(f'проиницилизированный список{init_list_people}')

