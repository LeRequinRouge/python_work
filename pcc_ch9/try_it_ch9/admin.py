from users import User


# admin class that inherits from User
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


admin_user = Admin("Cuda", "Requin", 0, "notyourtypicalcrow@gmail.com")
admin_user.privileges.show_privileges()
