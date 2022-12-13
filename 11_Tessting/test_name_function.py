import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''Тесты для 'name_function.py'.'''

    def test_first_last_name(self):
        '''Имена вида 'Janis Joplin' работает правильно? '''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '_main_':
    unittest.main()