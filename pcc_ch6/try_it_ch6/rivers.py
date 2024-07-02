rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'volga': 'russia'
}

# concise loop to print each river/country
for river, country in rivers.items():
    print(f"The {river.title()} river runs through {country.title()}.")

