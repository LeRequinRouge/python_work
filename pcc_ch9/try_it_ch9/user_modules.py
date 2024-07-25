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


class Admin(User):
    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
        ]

    def show_privileges(self):
        print(f"The user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")