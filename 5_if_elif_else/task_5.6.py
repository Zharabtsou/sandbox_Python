age = int(input('введите вашь возвраст: '))
if age < 2:
    print('младенец')
elif 2 <= age < 4:
    print('малыш')
elif 4 <= age < 13:
    print('ребенок')
elif 13 <= age < 20:
    print('подросток')
elif 20 <= age < 65:
    print('взрослый')
elif 65 <= age:
    print('пожилой человек')
