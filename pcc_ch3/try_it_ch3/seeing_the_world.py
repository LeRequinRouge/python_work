# prints the raw unordered contents of a list of places that
# I would like to visit.
places_to_see = ['paris', 'monaco', 'kyoto', 'turkey', 'greenland']
print(places_to_see)

# sorts the list without modifying permanently
print(sorted(places_to_see))
print(places_to_see)

# sorts the list in reverse alphabetical order without modification
print(sorted(places_to_see, reverse=True))
print(places_to_see)

# reverse order with permanent alteration
places_to_see.reverse()
print(places_to_see)

# reversing again to original state
places_to_see.reverse()
print(places_to_see)

# alphabetical sorting permanently
places_to_see.sort()
print(places_to_see)

# reverse alphabetical sorting permanently
places_to_see.sort(reverse=True)
print(places_to_see)



