list_user = []
list_password = []
new_user = True
while new_user:
    print('1 - добавить нового пользователя')
    print('2 - войти')
    print('3 - окончание сеанса')
    var = input('Введите: ')
    if not list_user:
        print('список пуст')
