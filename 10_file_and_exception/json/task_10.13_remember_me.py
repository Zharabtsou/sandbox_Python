import json

def get_stored_username():
    """Получает храниемое имя пользователя если оно существует"""
    filename = 'task_10_13_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Запрашивает новое имя пользователя если его нет в файле"""
    username = input('Как тебя зовут? ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user(name):
    '''Приветсвует пользователя по именни'''
    username = get_stored_username()
    if username:
        print(f'С возвращением {username}!')
    else:
        username = get_new_username()
        print(f'Мы тебя запомним если ты вернешся, {username}!')

