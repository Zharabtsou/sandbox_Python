human = {
    'first_name' : 'Андрей',
    'last_name': 'Жеребцов',
    'age': '32',
    'citi': 'Minsk',
    }

#вывод значение словоря по ключу
print(human['first_name'])
print(human['last_name'])
print(human['age'])
print(human['citi'])
print()
#вывод значений словора через запрос get + ключь
print(human.get('first_name'))
print(human.get('last_name'))
print(human.get('age'))
print(human.get('citi'))
print()

# get полезен тем что при отсутсвии такого ключа или значения в ключе можно прописать что вывести или вывести значение по умолчанию "None"
print(human.get('ceti'))
print(human.get('ceti', 'ceti!!!'))

human['status'] = 'father'

print(human)