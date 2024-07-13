def describe_city(name, country='russia'):
    print(f"{name.title()} is in {country.title()}")


describe_city('moscow')
describe_city(name='st. petersburg')
describe_city(country='United States', name='hawaii')
