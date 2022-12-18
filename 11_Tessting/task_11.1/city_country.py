def get_city_country(city, country, population=''):
    '''Строит отформотированное название города и страны'''
    if population:
        city_country = f'{city} {country} {population}'
    else:
        city_country = f'{city} {country}'
    return city_country.title()

