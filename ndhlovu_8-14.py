def car_information(manufacturer,model_name, **car_data):
    car_data['Manufacturer'] = manufacturer
    car_data['Model_name'] = model_name
    return car_data

car_info = car_information('BMW','M-Class',
    color = 'Yellow',
    tow_package = False,
    pre_owned = True
    )

print(car_info)
