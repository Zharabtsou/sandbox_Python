import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input('Как тебя зовут? ')
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f'Мы тебя запомним если ты вернешся, {username}!')
else:
    print(f'С возвращением {username}!')