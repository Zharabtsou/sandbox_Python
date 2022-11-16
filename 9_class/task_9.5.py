import car

my_beetle = car.Car('volvo', 'xc70', 2021)
print(my_beetle.get_descriptive_name())

my_electricCar = car.ElectricCar('tesls', 'T', 2010)
print(my_electricCar.get_descriptive_name())