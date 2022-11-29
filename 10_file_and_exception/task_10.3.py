def summa_int(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print(f'введите число')
    else:
        print(num1+num2)

summa_int(1,'sdsdf')
summa_int(25,30)
summa_int('122',45)
summa_int('fgdg',2)