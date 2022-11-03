def get_full_name(first_name, last_name):
    '''
    Функция получает имя м фамилию и возвращает одьедененное с заглавными буквами
    :param name:
    :param last_name:
    :return:
    '''
    full_name = (f'{last_name} {first_name}')
    return full_name.title()

person_name = get_full_name('andrey','zharabtsou')
print(person_name)

