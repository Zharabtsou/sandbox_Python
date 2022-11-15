class User():
    def __init__(self, first_name, last_name, age, local):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.local = local

    def user_info(self):
        print(f'First name: {self.first_name}')
        print(f'Last name: {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Local: {self.local}')

    def greet_user(self):
        print(f'\nHellow {self.first_name}')


user1 = User('Андрей', 'Жеребцов', '32', 'BY')
user2 = User('Алексей', 'Лукомский', '33', 'RU')
user3 = User('Александр', 'Кряжев', '30', 'BY')

user1.greet_user()
user1.user_info()

user2.greet_user()
user2.user_info()

user3.greet_user()
user3.user_info()