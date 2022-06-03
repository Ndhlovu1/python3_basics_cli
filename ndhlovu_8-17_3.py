def city_country_link(city,country):
    c_contr = (f"{city.title()}, {country.title()}")
    print("***************************************\nBelow are a couple of Cities some Countries\n***************************************\n")
    print(f'{c_contr}\n')

city_country_link(city=input("Please Enter a City\n"),country=input("Please Enter a Country\n") )

city_country_link('"Windhoek"', '"Namibia"')

city_country_link('"Khazakhistan"', '"Middle East"')
