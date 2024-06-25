name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())
print(f"Hello, {full_name.title()}!")

# f"" (format) combines strings
message = f"Hello, {full_name.title()}!"
print(message)

# \t adds whitespace (tab)
print("Python")
print("\tPython")
print("\t\tPython")

# \n adds a newline
print("Languages:\nPython\nC\nJavaScript")

# \n\t combo first sets a newline and then indents
print("test:\n\tdid this work?")

# \t\n combo indents and then newline (which isn't very useful)
print("test:\t\nwhat changed?")

# rstrip() method gets rid of whitespace temporarily
favorite_language = "Python "
print(favorite_language)
print(favorite_language.rstrip())

# Gets rid of white space permanently from the left
favorite_language = favorite_language.rstrip()
print(favorite_language)

# Gets rid of whitespace on the left
favorite_language = " Python "
print(favorite_language)
print(favorite_language.lstrip())

# Gets rid of whitespace on both sides
print(favorite_language.strip())
