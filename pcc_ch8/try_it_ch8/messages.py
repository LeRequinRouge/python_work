def show_messages(short_texts):
    for texts in short_texts:
        print(texts)


text_messages = [
    "Howdy!",
    "How are you?",
    "Where's the sun?",
    "Temples are impressive."
]

sent_messages = []

show_messages(text_messages)


# sending messages portion 8-10
def send_messages(short_texts, sent_texts):
    while short_texts:
        sent = short_texts.pop()
        sent_texts.append(sent)


# archived portion involves passing a
# spliced copy of the original list
# to the functions to maintain the original data
send_messages(text_messages[:], sent_messages)
print("\nThis is the original list of messages: ")
show_messages(text_messages)
print("\nThis is the sent list of messages: ")
show_messages(sent_messages)

