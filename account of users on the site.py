# A
class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print("User's full name: {} {}".format(self.first_name, self.last_name))
        print("Age: {}".format(self.age))
        print("Country: {}".format(self.country))

    def greeting_user(self):
        print("Hello, {}!".format(self.first_name))


user1 = User("Olenka", "Oleksyshyna", 17, "Ukraine")
user2 = User("Evelin", "Vladiyan", 16, "Ukraine")
user3 = User("Oleksii", "Kalunyk", 19, "Spain")

user1.describe_user()
user1.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()


# B
class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User("Olenka", "Oleksyshyna", 17, "Ukraine")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login attempts: {}".format(user1.login_attempts))

user1.reset_login_attempts()

print("Login attempts after reset: {}".format(user1.login_attempts))

# C
class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        print("Admin's privileges:")
        for privilege in self.privileges:
            print("- {}".format(privilege))


admin = Admin("Andrii", "Oleksyshyn", 49, "Ukraine")
admin.show_privileges()

# D
class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


admin = Admin("Andrii", "Oleksyshyn", 49, "Ukraine")
admin.privileges.show_privileges()

# E

from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()
