current_users = ['bill', 'tom', 'admin', 'felix', 'clair']
new_users = ['janet', 'BILL', 'ralph', 'Clair', 'amanda']

for user in new_users:
    if user.lower() in current_users:
        print("Sorry, but that username is unavailable.")
    else:
        print("That username is available!")
        current_users.append(user.lower())

print(current_users)

