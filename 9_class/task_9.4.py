from electric_car import ElectricCar


car3 = ElectricCar('tesla', 'T2', 2020)
print(car3.get_descriptive_name())
car3.read_odometer_reading()
car3.battary.battery_size(5500)
car3.geet_battery()
car3.increment_odometer(1000)
car3.read_odometer_reading()
