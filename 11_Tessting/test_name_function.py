import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''Тесты для 'name_function.py'.'''

    def test_first_last_name(self):
        '''Имена вида 'Janis Joplin' работает правильно? '''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle(self):
        '''Имена вида 'Janis Joplin Jonni' работает правильно? '''
        formatted_name = get_formatted_name('janis', 'joplin', 'jonni')
        self.assertEqual(formatted_name, 'Janis Joplin Jonni')

if __name__ == '_main_':
    unittest.main()