def count_words(filename):
    """Посчет преблезительного количество слов"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
        #открывает фаил и присваевает его содержание этих файлов переменной contents
    except FileNotFoundError:
        print(f'Sorry, the file {filename} doest not exist.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

filename = 'gram.txt'
count_words(filename)