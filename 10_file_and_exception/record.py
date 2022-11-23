filename = 'program.txt'

with open(filename, 'w') as file_object:
    masseg = int(input('Введите число: '))
    str_masseg = str(masseg)
    file_object.write(str_masseg)

print('The end')