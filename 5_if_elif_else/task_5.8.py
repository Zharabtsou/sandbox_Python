list_user = ['admin']
list_password = ['admin']

while True:
    if not list_user:
        print('Список пользователь пуст создайте нового пользователя')
        user = input('Введите имя нового пользователя: ')
        list_user.append(user)
        user_password = input('Введите пароля: ')
        list_password.append(user_password)
    print('\nдобрый день вас приветсвуент программа эмулятор регистрации пользователей')
    print('1 - добавить нового пользователя')
    print('2 - удалить пользователя')
    print('3 - войти')
    print('4 - окончание сеанса')

    var = int(input('Введите: '))

    if var == 1:
        user = input('Введите имя нового пользователя: ')
        if user.lower() not in list_user:
            list_user.append(user.lower())
            password = input('Введите пароль: ')
            list_password.append(password)
        else:
            print('Пользователь с таким именем уже есть')

    elif var == 2:
        id = 0
        del_user = input('введите имя пользователя которого вы хотите УДАЛИТЬ: ')
        if del_user.lower() in list_user:
            for item in list_user:
                if item != del_user.lower():
                    id += 1
                else:
                    item_pass = 0
                    while item_pass < 3:
                        del_password = input('введите пароль пользователя для удаления: ')
                        if list_user[id] == del_user.lower() and list_password[id] == del_password:
                            list_user.pop(id)
                            list_password.pop(id)
                            print(f'пользователь с именем {del_user.title()} был удален')
                            item_pass = 4
                        else:
                            print('не верный пароль попытайтесь еще')
                            item_pass += 1
        else:
            print(f'пользователя с именем "{del_user.title()}" не существует')

    elif var == 3:
        id = 0
        login_user = input('введите имя пользователя для входа: ')
        if login_user.lower() in list_user:
            for item in list_user:
                if item != login_user.lower():
                    id += 1
                else:
                    item_pass = 0
                    while item_pass < 3:
                        login_password = input('введите пароль пользователя для удаления: ')
                        if list_user[id] == login_user.lower() and list_password[id] == login_password:
                            print(f'Добро пожаловать {login_user.title()} !!!')
                            item_pass = 4
                        else:
                            print('не верный пароль попытайтесь еще')
                            item_pass += 1
        else:
            print(f'пользователя с именем "{login_user.title()}" не существует')

    elif var == 4:
        print('Спасибо за работу досвидание')
        break

    else:
        print(list_user)
        print(list_password)