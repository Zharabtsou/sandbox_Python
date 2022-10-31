favorite_places = {
    'Minsk': ['Andrey', 'Sasha', 'Lena'],
    'Grodno': ['Andrey','Sasha'],
    'Gomel': ['Serhey','Maksim'],
    }

for siti, name in favorite_places.items():
    print(f"{siti.title()} нравится:")
    for item in name:
        print(f"\t{item.title()}")