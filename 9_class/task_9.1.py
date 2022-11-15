class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def descride_restaurant(self):
        print(f'Название ресторана {self.restaurant_name}')
        print(f'время работы {self.cuisine_type}')

    def open_restaurant(self):
        print(f'ресторан {self.restaurant_name} открыт')



