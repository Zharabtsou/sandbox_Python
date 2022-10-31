people = {
    'Andrey': {
        'first_name' : 'Андрей',
        'last_name': 'Жеребцов',
        'age': '32',
        'citi': 'Minsk',
        },
    'Ivan': {
        'first_name' : 'иванов',
        'last_name': 'Иван',
        'age': '22',
        'citi': 'Gomel',
        },
    'Aleksandr':  {
        'first_name' : 'Александр',
        'last_name': 'Кряжев',
        'age': '31',
        'citi': 'Jlobin',
        },
    }

for name,info in people.items():
    print(name.title())
    for key, info in info.items():
        print(f"\t{key.title()}: {info.title()}")