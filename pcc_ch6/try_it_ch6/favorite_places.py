# storing a list inside a dictionary
favorite_places = {
    'drew': ['ocean beach', 'hawaii'],
    'leah': ['isla vista', 'sea cliff', 'solvang'],
    'filipe': ['guadalajara']
}

for people in favorite_places:
    print(f"\n{people.title()}'s favorite place(s) to visit are: ")
    for place in favorite_places[people]:
        print(f"\t{place.title()}")

