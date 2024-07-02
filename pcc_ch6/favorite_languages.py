favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

# for loop addition to access all keys and values
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# key() method usage
# which returns the name of the key
# note: key is returned by default (e.g. for name in favorite_languages:)
# therefore key() may be omitted
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print("Hi",name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# dictionaries can be sorted using the sorted() method
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

# value() method can access all second statements in a dictionary
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# a set() method can be used to prevent repetition
for language in set(favorite_languages.values()):
    print(language.title())

# nesting provides multiple answers to the poll
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language(s) are:")
    for language in languages:
        print(f"\t{language.title()}")
