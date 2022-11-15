class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descride_restaurant(self):
        print(f'\nНазвание ресторана {self.restaurant_name}')
        print(f'время работы {self.cuisine_type}')

    def open_restaurant(self):
        print(f'ресторан {self.restaurant_name} открыт')



res1 = Restaurant('Сладко', '11:30-19:00')
res2 = Restaurant('Слон', '20:00-5:00')
res3 = Restaurant('1+1','24')


res1.descride_restaurant()
res1.open_restaurant()

res2.descride_restaurant()
res2.open_restaurant()

res3.descride_restaurant()
res3.open_restaurant()