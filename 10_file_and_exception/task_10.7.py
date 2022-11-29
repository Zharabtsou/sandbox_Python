while True:
    try:
        print('Сложим числа')
        num1 = int(input('введите число №1: '))
        num2 = int(input('введите число №2: '))
    except ValueError:
        text = 'введите число!!!!'
        print(text.upper())
    else:
        print(f'сумма {num1} + {num2} = {num1+num2}')
        break
