# dictionaries within a dictionary with a city theme
cities = {
    'seattle': {
        'country': 'united states',
        'population': 750000,
        'fact': 'there is an old city underneath it',
    },
    'san diego': {
        'country': 'united states',
        'population': 1380000,
        'fact': 'home of the padres baseball team'
    },
    'tokyo': {
        'country': 'japan',
        'population': 13960000,
        'fact': 'used to be called edo'
    },
}

# loops through nested dictionaries (honestly takes
# a bit for me to figure out the moving parts...)
# added conditional statements to capitalize the
# country portion of the city info.
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    for info in cities[city]:
        if info == 'country':
            print(f"\t{info.title()}: {city_info[info].title()}")
        else:
            print(f"\t{info.title()}: {city_info[info]}")
