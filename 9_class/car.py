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

    def car_fill(self, fill):
        self.fill = fill

    def get_fill(self):
        print(f'размер бака {self.make} состовляет {self.fill} литров')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battary = Battary()

    def geet_battery(self):
        print(f'{self.make} установлена батарея размером {self.battary.size} литров')

    def get_fill(self):
        print(f'У электромобиля марки {self.make} нет бака!!! Там батарея размером {self.battary.size} Ah')

class Battary():

    def battery_size(self, size=100):
        self.size = size


# car1 = Car('Audi', 'C8', 2015)
# print(car1.get_descriptive_name())
# car1.read_odometer_reading()
# car1.increment_odometer(500)
# car1.read_odometer_reading()
# car2 = ElectricCar('tesla', 'T2', 2020)
# print(car2.get_descriptive_name())
# car2.read_odometer_reading()
# car2.battary.battery_size(5500)
# car2.geet_battery()
# car2.increment_odometer(1000)
# car2.read_odometer_reading()
# car1.car_fill(50)
# car1.get_fill()
# car2.get_fill()

