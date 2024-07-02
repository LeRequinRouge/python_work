# more dictionary practice
# program stores fictional people's favorite number
# additional 6-10 amendment involving nesting
people = {'fred': [7,88],
          'ari': [99, 100, 101],
          'drew': [6, 66],
          'rona': [19],
          'steph': [1000, 4545, 11, 27]
          }

# this code is cleaner with only 1 number per person
print(people)
print(f"Fred's favorite number is {people['fred']}.")
print(f"Ari's favorite number is {people['ari']}.")
print(f"Drew's favorite number is {people['drew']}.")
print(f"Rona's favorite number is {people['rona']}.")
print(f"Steph's favorite number is {people['steph']}.")

# concise looping involving multiple values per key
for peeps in people:
    print(f"\n{peeps.title()}'s favorite number(s) are:")
    for number in people[peeps]:
        print(f"\t{number}")

