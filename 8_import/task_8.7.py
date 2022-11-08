from pizza_import import make_user
from pizza_import import make_user as m_u
import pizza_import
import pizza_import as p_i


info = make_user('андрей', 'жеребцов', age = '22', lang = 'ru')

for key,inf in info.items():
    print(f'{key.title()}: {inf.title()}')

info = m_u('andreu', 'zherebtsou', age = '22', lang = 'en')

for key,inf in info.items():
    print(f'{key.title()}: {inf.title()}')

pizza_import.make_pizza(22,'огурец', 'помидор')
p_i.make_pizza(36,'лосось', 'сыр')