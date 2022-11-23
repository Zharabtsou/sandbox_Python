filename = 'program.txt'

with open(filename, 'a') as file_object:
    masseg = ''
    while masseg != 'quit':
        if masseg != 'quit':
            file_object.write(f'{masseg}\n')
        masseg = input('Введите сообщение: ')

print('The end')