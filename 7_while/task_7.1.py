while True:
    print('для завершения програмы введите "quit"!!!!')
    masseg = input('Что вы бы хотели добавить в пицу: ')
    if masseg == 'quit':
        break
    else:
        print(f'В заказ будет добавлено {masseg}')

print('\nСпасибо за заказ досвидание')