# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
countries_cities = {
    "Belarus": ["Minsk", "Gomel", "Borisov", "Grodno", "Vitebsk"],
    "Poland": ["Warsaw", "Krakow", "Bialystok", "Wroclaw", "Gdansk"],
    "Ukraine": ["Kyiv", "Kharkiv", "Odesa", "Lviv", "Kherson"],
    "Iceland": ["Reykjavik", "Kopavogur", "Akranes", "Akureyri", "Arborg"],
    "Sweden": ["Stockholm", "Gothenburg", "Kalmar", "Lund", "Sala"],
}
city_input = input("Enter a city: ")


def foo(country, city):
    for key, value in countries_cities.items():
        if city_input in value:
            return key


print(f"{city_input} is in {foo(countries_cities, city_input)}")
