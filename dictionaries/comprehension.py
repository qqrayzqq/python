# dictionary comprehension =    dictionary = {key: expression for (key, value) in iterable}

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}
print(cities_in_C)

# dictionary = {key: expression for (key, value) in iterable if conditional}

weather = {'New York': 'snowing', 'Boston': 'sunny', 'Los Angeles': 'sunny', 'Chicago': 'cloudy'}
sunny_weather = {key: value for (key, value) in weather.items() if value == 'sunny'}
print(sunny_weather)

# dictionary = {key: (if/else) for (key, value) in iterable}

cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_upgraded = {key: ("Warm" if value >= 50 else "Cold") for (key, value) in cities.items()}
print(cities_upgraded)

# dictionary = {key: function(value) for (key, value) in iterable}


def check_temp(value):
    if value >= 75:
        return "Warm"
    else:
        return "Cold"


cities2 = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities2_upgraded = {key: check_temp(value) for (key, value) in cities2.items()}
print(cities2_upgraded)
