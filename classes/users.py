class User:

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        if self.__check_mail(email):
            self.email = email
        else:
            raise ValueError("Bad format of email")

    def change_password(self):
        while True:
            email_check = str(input(f"Hi {self.username}, write your email: \n"))
            if email_check != self.email:
                print("It's not your email\n")
            else:
                print("Fine")
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
        cnt = 0
        while True:
            email_check = str(input(f"Hi {self.username}, write your new email: \n"))
            if self.__check_mail(email_check):
                if email_check == self.email:
                    print("It's your old email.")
                else:
                    self.email = email_check
                    print("It OK\n")
                    break
            else:
                print("Maybe you missclicked, try again.")
                cnt += 1
            if cnt == 3:
                raise ValueError("Try again later.")

    def check_password(self, new_password):
        return new_password == self.password

    @staticmethod
    def __check_mail(mail: str) -> bool:
        correct_formats = ["@gmail.com", "@yandex.ru", "@yahoo.com"]
        for char in mail:
            if char == '@':
                index_of_rate = mail.index(char)
                after_rate: str = mail[index_of_rate:]
                if after_rate not in correct_formats:
                    return False
                else:
                    return True
            else:
                pass
        return False

    def display_info(self):
        print(f"Username: {self.username}")
        answers = ["Yes", "yes", "YES", "YeS", "yES", "yEs", "yeS"]
        display_passwd = str(input("Do you want to see your passwd?"))
        if display_passwd in answers:
            email_check = str(input("Write your email to see your password:"))
            if email_check == self.email:
                print(f"Ok. Here is your password: {self.password}")
            else:
                print("Sorry it's not your email.")


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
