# this program makes a list of people (either living or deceased) to dinner and
# then prints a message for each object/person.
# additionally, one of the guests can't make it so we must modify the list.

guest_list = ['wayne gretzky', 'barrack obama', 'helen*? keller']
message1 = f"Hello, {guest_list[0].title()}! Let's talk Edmonton over dinner sometime.\n"
message2 = f"We miss you, {guest_list[1].title()}, how about a beer?\n"
message3 = f"*Jazz hands* {guest_list[2].title()} *Jazz hands*\n"

print(message1, message2, message3)
declined_guest = guest_list[2]
declined_invite = f"Unfortunately {declined_guest} can't make it =("
print(declined_invite)

guest_list.remove(declined_guest)
guest_list.append('Sterling Archer')
message3 = f"I know this is how we get ants... but i'd like for you to come anyways, {guest_list[2]}"
print(message1, message2, message3)