# stemming from 6-1, storing dictionaries
# representing a person into a list of people
leah_beisel = {'first_name': 'leah',
               'last_name': 'beisel',
               'age': 29,
               'city': 'wrightwood',
               }

drew_croteau = {
    'first_name': 'drew',
    'last_name': 'croteau',
    'age': 30,
    'city': 'wrightwood',
}

caleb_lee = {
    'first_name': 'caleb',
    'last_name': 'lee',
    'age': 30,
    'city': 'wrightwood',
}

# list storing the dictionaries of each person
people = [leah_beisel, drew_croteau, caleb_lee]

# loop that prints the information of all people
for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} "
          f"is {person['age']} and lives in {person['city'].title()}.")



