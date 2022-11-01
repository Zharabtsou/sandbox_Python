glossary_list = {
    'python': 'это высокоуровневый язык программирования общего назначения, который используется в том числе и для  '
              'разработки веб-приложений. Язык ориентирован на повышение производительности разработчика и читаемости кода.'
}



for key in glossary_list:
   print(f'{key.title()} - {glossary_list.get(key)}')


glossary_list.update({'бежал': 'бежать в прошедшем времени',
                   'туфли': 'туфля во множественном числе'})

for key in glossary_list:
   print(f'{key.title()} - {glossary_list.get(key)}')
