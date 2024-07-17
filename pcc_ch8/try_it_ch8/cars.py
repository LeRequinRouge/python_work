def make_car(make, model, **info):
    info['make'] = make
    info['model'] = model
    return info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
car_2 = make_car('honda', 'civic', color='grey', year=2012, miles=163000)
print(car_2)