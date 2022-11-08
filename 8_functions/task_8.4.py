def pizza(size, *args):
    print(f'Размер {size} и список ингридиентов:')
    for arrg in args:
        print(f'\t{arrg}')





pizza(12, 'перец', 'колбаски', 'лук', 'огурец',)