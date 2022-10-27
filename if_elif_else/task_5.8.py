list_user = []
list_password = []
new_user = True
while new_user:
    if not list_user:
        print('Список пользователь пуст создайте нового пользователя')
        user = input('Введите имя нового пользователя: ')
        list_user.append(user)
        user_password = input('Введите пароля: ')
        list_password.append(user_password)
    print('добрый день вас приветсвуент программа эмулятор регистрации пользователей')
    print('1 - добавить нового пользователя')
    print('2 - удалить пользователя')
    print('3 - войти')
    print('4 - окончание сеанса')
    var = int(input('Введите: '))



    if var == 4:
        print('Спасибо за работу досвидание')
        break


