# introduction to functions
def greet_user():
    """Display a simple greeting."""
    print("Hello, user!")


greet_user()


# function that receives data
def greet_user(username):
    """Display a simple greeting after receiving data."""
    print(f"Hello, {username.title()}!")


greet_user("jesse")
