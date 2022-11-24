from datetime import datetime
filename = 'program.txt'
masseg = 'Start'
with open(filename, 'a') as file_object:
    while masseg != 'quit':
        if masseg != 'quit':
            file_object.write(f'{datetime.now()}: {masseg}\n')
        masseg = input('Введите сообщение: ')
    file_object.write(f'{datetime.now()}: STOP\n')
print('The end')
