'''
dictionary comprehensions : are used for making dicts with less syntax, also can apply a layer of logic and create new dicts

WAYS:
    {key:expression for (key,value) in iterable }
    {key:expression for (key,value) in iterable if conditional}
    {key:expression (if/else) for (key,value) in iterable}
    {key:call_func(value) for (key,value) in iterable}
    
    **if iterable is dictionary use .items
'''
# EXAMPLE 1
cities_in_F = {
                "New York": 80,
                "Los Angeles": 75,
                "Chicago": 72,
                "Miami": 85,
                "Dallas": 90
              }
print(cities_in_F)
cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------- EXAMPLE 2
weather_cities = {
                "New York": "cold",
                "Los Angeles": "hot",
                "Chicago": "cold",
                "Miami": "hot",
                "Dallas": "cold"
              }
weather = {key: value for (key,value) in weather_cities.items() if value == "hot" }
print(weather)

# -------------------------- EXAMPLE 3

temperature = {
                "New York": 80,
                "Los Angeles": 75,
                "Chicago": 72,
                "Miami": 85,
                "Dallas": 90
              }
print(temperature)
temp_check = {key: "hot" if value >=80 else "cold" for (key,value) in temperature.items()}
print(temp_check)

# -------------------------- EXAMPLE 4

# calling a function: in a dictionary

def check_temp(value):
    if value >= 80:
        return "hot"
    else:
        return "coldddd"
    
temperature_cities = {
                "New York": 80,
                "Los Angeles": 75,
                "Chicago": 72,
                "Miami": 85,
                "Dallas": 90
              }
print(temperature)
temp_show = {key: check_temp(value) for (key,value) in temperature.items()}
print(temp_show)