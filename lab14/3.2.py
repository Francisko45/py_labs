class User:
    def __init__(self, a, b):
        self.first_name = a
        self.last_name = b
        self.login_attempts = 0

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



a = User("Alice", "Johnson")
b = User("Bob", "Smith")


a.describe_user()
a.greet_user()


a.increment_login_attempts()
a.increment_login_attempts()
print(f"Login attempts: {a.login_attempts}")
a.reset_login_attempts()
print(f"Login attempts after reset: {a.login_attempts}")


class Privileges:
    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, a, b):
        super().__init__(a, b)
        self.privileges = Privileges()



a = Admin("Admin", "User")
a.privileges.privileges = [
    "Can add post",
    "Can delete post",
    "Can ban user"
]
a.describe_user()
a.privileges.show_privileges()
