# copied code from favorite_languages.py for 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jared': 'c#',
    'janet': 'java',
    'john': 'c++',
    'melissa': 'swift',
    'randy': 'java'
}

polling_prospects = [
    'jen',
    'ridley',
    'ken',
    'sarah',
    'chuck',
    'lucy',
    'randy'
]

# loop to check if polling prospects have already voted
for name in polling_prospects:
    if name not in favorite_languages.keys():
        print(f"{name.title()}, it would seem you haven't voted yet... Please do!")
    else:
        print(f"Thank you for taking our poll, {name.title()}!")
