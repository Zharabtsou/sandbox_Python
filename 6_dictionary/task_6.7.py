human_01 = {
    'first_name' : 'Андрей',
    'last_name': 'Жеребцов',
    'age': '32',
    'citi': 'Minsk',
    }
human_02 = {
    'first_name' : 'иванов',
    'last_name': 'Иван',
    'age': '22',
    'citi': 'Gomel',
    }
human_03 = {
    'first_name' : 'Александр',
    'last_name': 'Кряжев',
    'age': '31',
    'citi': 'Jlobin',
    }
people = [human_01, human_02, human_03]

for item in people:
    for key, info in item.items():
        print(f'{key}:{info.title()}')

    print()