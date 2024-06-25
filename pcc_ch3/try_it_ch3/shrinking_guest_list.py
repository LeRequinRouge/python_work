# this program makes a list of people (either living or deceased) to dinner and
# then prints a message for each object/person.
# additionally, one of the guests can't make it, so we must modify the list using remove() and append() methods.
# we found a bigger table, so now we can invite more guests! utilizing insert() and append() methods.
# the table won't make it in time, however, so now we must modify the list so only 2 invitations can be sent.

# tailored messages for each guest.
guest_list = ['wayne gretzky', 'barrack obama', 'helen*? keller']
message1 = f"Hello, {guest_list[0].title()}! Let's talk Edmonton over dinner sometime.\n"
message2 = f"We miss you, {guest_list[1].title()}, how about a beer?\n"
message3 = f"*Jazz hands* {guest_list[2].title()} *Jazz hands*\n"

print(message1, message2, message3)
declined_guest = guest_list[2]
declined_invite = f"Unfortunately {declined_guest} can't make it =("
print(declined_invite)

guest_list.remove(declined_guest)
guest_list.append('sterling archer')
message3 = f"I know this is how we get ants... but i'd like for you to come anyways, {guest_list[2]}"
print(message1, message2, message3)

# since more guests are being added we'll need a more generic invitation.
guest_list.insert(0, 'leah beisel')
guest_list.insert(2, 'jack the ripper')
guest_list.append('rihanna')

print(guest_list)
print('\n')

# inefficient without the use of for loop
message = "You're formally invited to have dinner with me, "
print(f"{message}{guest_list[0].title()}!")
print(f"{message}{guest_list[1].title()}!")
print(f"{message}{guest_list[2].title()}!")
print(f"{message}{guest_list[3].title()}!")
print(f"{message}{guest_list[4].title()}!")

print('\n')

# a message for each dropped guest that's popped from the end of the list
print("I'm terribly sorry, but the table won't arrive for another week. There's only room for 2 guests.")
message = "Sorry, your dinner access is being revoked, "
print(f"{message}{guest_list.pop().title()}")
print(f"{message}{guest_list.pop().title()}")
print(f"{message}{guest_list.pop().title()}")

# messaging the remaining guests
message = "Congratulations! You're still invited to dinner, "
print(f"{message}{guest_list[0].title()} and {guest_list[1].title()}!")

# deleting the remaining objects from the list and checking to see if it's empty
del guest_list[0, 1]
print(guest_list)