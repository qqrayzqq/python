class User:

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email

    def change_password(self):
        while True:
            email_check = str(input(f"Hi {self.username}, write your email: \n"))
            if not self.check_mail(email_check):
                print("It's not your email\n")
            else:
                break
        while True:
            new_password = input("Print your new password:\n")
            if self.check_password(new_password):
                print("You can't make new password like your old password:\n")
            else:
                self.password = new_password
                print("It's OK\n")
                break

    def change_email(self):
        while True:
            email_check = str(input(f"Hi {self.username}, write your new email: \n"))
            if self.check_mail(email_check):
                print("It's your old email\n")
            else:
                self.email = email_check
                print("It OK\n")
                break

    def check_password(self, new_password):
        return new_password == self.password

    def check_mail(self, new_email):
        return new_email == self.email

    def display_info(self):
        print(f"Username: {self.username}, email: {self.email}")
        answers = ["Yes", "yes"]
        display_passwd = str(input("Do you want to see your passwd?"))
        if display_passwd in answers:
            print(f"Here is your passwd: {self.password}")


def create_user(username, email, password):
    return User(username, email, password)


if __name__ == '__main__':
    user1 = create_user("rayzqq", "asirbabayanvlad@gmail.com", "a02082005A")
    user2 = create_user("bambo", "bimba@yandex.ru", "nbhq81b")
    user3 = create_user("mindan", "minakov.danil@yahoo.com", "balinday_3")
    user1.change_email()
    user2.change_password()
    user1.display_info()
    user2.display_info()
    user3.display_info()
