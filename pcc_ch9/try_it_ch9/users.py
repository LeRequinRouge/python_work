class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = int(age)
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("User information:")
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Welcome back, {self.first_name} {self.last_name}!\n")

    def increment_login_attempts(self, logins):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Drew", "Croteau", 30, "requin@csu.fullerton.edu")
user1.describe_user()
user1.greet_user()

user2 = User("Leah", "Beisel", 29, "leah.promo24@gmail.com")
user2.describe_user()
user2.greet_user()

user3 = User("Bob", "Belcher", 46, "bbelcherburgers@goodeats.com")
user3.describe_user()
user3.greet_user()

# Login Attempts 9-5 increment modification & reset
user4 = User("Timothy", "Mewtron", 6, "shampooisbetta@catfax.com")
for mews in range(0, 5):
    user4.increment_login_attempts(mews)
print(user4.login_attempts)

user4.reset_login_attempts()
print(user4.login_attempts)