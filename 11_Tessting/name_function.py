def get_formatted_name(first, last, meddle = ''):
    '''Строит отформотированное полное имя'''
    if meddle:
        full_name = f'{first} {last} {meddle}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()