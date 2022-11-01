price = ['бесплатно', 10, 15]

while True:
    age = int(input('Введите свой возвраст: '))
    if age < 3:
        print(price[0])
    elif age >=3 and age <= 12:
        print(price[1])
    elif age > 99:
        print('Может пора уже задуматся?)))')
        break
    else:
        print(price[2])

