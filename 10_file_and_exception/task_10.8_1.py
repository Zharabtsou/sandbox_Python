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
        print('конец файла'.upper())

files = ['cat.txt', 'dog.txt', 'pet.txt']

for item in files:
    read_print(item)