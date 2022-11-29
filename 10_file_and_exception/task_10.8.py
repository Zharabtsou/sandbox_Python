def read_print(fil_name):
    try:
        with open(fil_name, encoding='utf-8') as text:
            content = text.read()
    except FileNotFoundError:
        print(f'\nфайла {fil_name} не удалось найти\n'.upper())
    else:
        words = content.split()
        for word in words:
            print(word)

file1 = 'cat.txt'
file2 = 'dog.txt'


read_print(file1)
read_print('file3.txt')
read_print(file2)