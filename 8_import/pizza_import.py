def make_pizza(size, *ings):
    print(f'\nРазмер пиццы {size}, в нее входит:')
    for ing in ings:
        print(f'\t{ing.title()}')


def make_user(firs, last, **user_info):
    user_info['first_name'] = firs
    user_info['last_name'] = last
    return user_info