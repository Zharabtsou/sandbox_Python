names = []
name = ''
while name != 'end':
    name = input('введите имя друга : ')
    names.append(name)

for friend_name in names:
    if friend_name == 'end':
        break
    else:
        print(f'Твоего друга зовут {friend_name.title()}')