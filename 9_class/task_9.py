class Dog():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over')


my_dog = Dog('bobi',15)

print(f'name {my_dog.name}')
print(f'old {my_dog.age}')

my_dog.sit()


mimi = Dog('karl', 44)
print(f'name {mimi.name}')
print(f'old {mimi.age}')

mimi.roll_over()