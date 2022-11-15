class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.make} {self.model} {self.year}'
        return long_name.title()

    def read_odometer_reading(self):
        print(f'на данный момент пробег {self.odometer_reading}')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def battery_size(self, size):
        self.size = size

    def geet_battery(self):
        print(f'{self.make} установлена батарея размером {self.size}')


car1 = Car('Audi', 'C8', 2015)
print(car1.get_descriptive_name())
car1.read_odometer_reading()
car1.increment_odometer(500)
car1.read_odometer_reading()

car2 = ElectricCar('tesla', 'T2', 2020)
print(car2.get_descriptive_name())
car2.read_odometer_reading()
car2.battery_size(5500)
car2.geet_battery()
car2.increment_odometer(1000)
car2.read_odometer_reading()

