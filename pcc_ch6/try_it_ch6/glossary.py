# storing python keywords as keys in a dictionary
# and then what they do as values
keywords = {'and': "Used in conditional statements for inclusion of all conditions before tripping.",
            'or': "Used in conditional statements that is tripped if at least one condition is met.",
            'del': "Used to delete data.",
            'if': "Used to setup the conditional environment. If the condition is met, nothing further is read.",
            'else': "If the if/elif conditional statements are not tripped, code within this block are executed.",
            'elif': "If the if statement isn't tripped then elif is tried next.",
            'for': "The start of a loop. Typically represents the values acquired.",
            'in': "Access the container that's subject to a loop",
            'not': "Used in conjunction with in to look for objects that are not with the data structure."
            }
print(f"and: {keywords['and']}.")
print(f"or: {keywords['or']}")
print(f"del: {keywords['del']}")
print(f"if: {keywords['if']}")
print(f"else: {keywords['else']}\n")

# 6-4 concise looped version
for keyword, definition in keywords.items():
    print(f"{keyword}: {definition}")