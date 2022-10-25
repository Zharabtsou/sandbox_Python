alien_color = input('введите цвет пришельцев grean yellow red: ')
if alien_color == 'green':
    print('Player earned 5 points')
elif alien_color == 'yellow':
    print('Player earned 10 points')
elif alien_color == 'red':
    print('Player earned 15 points')
else:
    print("I don't know this color")