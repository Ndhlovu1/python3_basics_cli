def city_country(city,country):
    c_contr = (f"{city.title()}, {country.title()}")
    print("***************************************\nBelow are a couple of Cities some Countries\n***************************************\n")
    print(f'{c_contr}\n')

city_country(city = input("Please Enter a City\n"),country = input("Please Enter a Country\n") )

city_country('"Windhoek"', '"Namibia"')

city_country('"Khazakhistan"', '"Middle East"')
