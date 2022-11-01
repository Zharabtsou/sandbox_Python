anfisa = {
    'breed': 'dog',
    'master': 'Andrey',
    }

ramsi = {
    'breed': 'dog',
    'master': 'Alex',
    }

tima = {
    'breed': 'cat',
    'master': 'Sveta',
    }
pets = [anfisa, ramsi, tima,]


for item in pets:
    for key, info in item.items():
        print(f'\t{key.title()}:{info.title()}')
