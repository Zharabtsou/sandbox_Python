import unittest
from city_country import get_city_country


class NameTestCase(unittest.TestCase):
    '''Тесты для 'city_country.py'.'''

    def test_city_country_population(self):
        '''название 'Buda Bellarus million' работает правильно? '''
        city_country = get_city_country('buda', 'bellarus', '5500')
        self.assertEqual(city_country, 'Buda Bellarus 5500')


    def test_city_country(self):
        '''название 'Buda Bellarus' работает правильно? '''
        city_country = get_city_country('Buda', 'Bellarus')
        self.assertEqual(city_country, 'Buda Bellarus')

if __name__ == '_main_':
    unittest.main()