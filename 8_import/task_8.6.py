import pizza_import


pizza_import.make_pizza(22,'огурец', 'помидор')

info = pizza_import.make_user('андрей', 'жеребцов', age = '22', lang = 'ru')
print(info)
for key,inf in info.items():
    print(f'{key.title()}: {inf.title()}')