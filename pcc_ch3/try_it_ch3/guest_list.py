# this program makes a list of people (either living or deceased) to dinner and
# then prints a message for each object/person.

guest_list = ['wayne gretzky', 'barrack obama', 'helen*? keller']
message1 = f"Hello, {guest_list[0].title()}! Let's talk Edmonton over dinner sometime.\n"
message2 = f"We miss you, {guest_list[1].title()}, how about a beer?\n"
message3 = f"*Jazz hands* {guest_list[2].title()} *Jazz hands*\n"

print(message1, message2, message3)