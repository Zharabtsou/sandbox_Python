fil_name = 'book.txt'
try:
    with open(fil_name, encoding='utf-8') as text:
        content = text.read()
except FileNotFoundError:
    print(f'\nфайла {fil_name} не удалось найти\n'.upper())
else:
    print(content.lower().count('s'))