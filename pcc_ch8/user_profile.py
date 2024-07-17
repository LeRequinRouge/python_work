def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert',
                             'einstein',
                             location='princeton',
                             field='physics')

# 8-13 addition about me!
my_profile = build_profile('drew',
                           'croteau',
                           age=30,
                           occupation='ski instructor',
                           food_preference='spicy')

print('\n', user_profile)
print('\n', my_profile)
