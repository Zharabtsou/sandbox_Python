my_favorite_fruit = ['bananas', 'apple', 'kiwi']

fruit = input('favorite fruit: ')
if fruit.lower() in my_favorite_fruit:
    print(f'You really like {fruit.title()}')