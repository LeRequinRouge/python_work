user_list = ['admin', 'jack', 'bs2', 'emilio', 'ari']

for user in user_list:
    if user == 'admin':
        print(f'Greetings, {user.upper()}! Care to see a status report?')
    else:
        print(f"Welcome back, {user.title()}!")

# no users section 5-9
user_list = []

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f'Greetings, {user.upper()}! Care to see a status report?')
        else:
            print(f"Welcome back, {user.title()}!")
else:
    print('There are no users!')