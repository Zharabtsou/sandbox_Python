from pizza_import import *

info = make_user('андрей', 'жеребцов', age = '22', lang = 'ru')

for key,inf in info.items():
    print(f'{key.title()}: {inf.title()}')