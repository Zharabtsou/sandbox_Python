def get_full_name(first_name, last_name, maddle_name = ''):
    '''
    Функция получает имя м фамилию и возвращает одьедененное с заглавными буквами
    :param name:
    :param last_name:
    :return:
    '''
    if maddle_name:
        full_name = (f'{last_name} {maddle_name} {first_name}')
    else:
        full_name = (f'{last_name} {first_name}')
    return full_name.title()

person_name = get_full_name(first_name = 'andrey', last_name= 'zharabtsou')
print(person_name)
person_madle_name = get_full_name('andrey', 'zharabtsou', 'подожди подожди',)
print(person_madle_name)