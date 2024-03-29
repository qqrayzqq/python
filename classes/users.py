import random
from datetime import datetime


class User:

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        if self.__check_mail(email):
            self.email = email
        else:
            raise ValueError("Bad format of email")

    @staticmethod
    def allchars(s):
        has_letters = any(char.isalpha() for char in s)
        has_digits = any(char.isdigit() for char in s)
        has_special_chars = not s.isalnum()
        return has_letters and has_digits and has_special_chars

    @staticmethod
    def mid_passwd(s):
        has_letters = any(char.isalpha() for char in s)
        has_digits = any(char.isdigit() for char in s)
        return has_letters and has_digits

    def change_password(self):
        cnt = 0
        while True:
            email_check = str(input(f"{self.username}, write your email: \n"))
            if not self.__check_mail(email_check):
                print("Invalid email\n")
                cnt += 1
            elif email_check == self.email:
                print("Fine")
                break
            elif email_check != self.email:
                print("It's not your email\n")
                cnt += 1
            if cnt == 5:
                print("Too many attempts, try again later.\n")
                return
        cnt = 0
        while True:
            new_password = input("Now print your new password:\n")
            if self.check_password(new_password):
                print("You can't make new password like your old password\n")
            else:
                while True:
                    if self.allchars(new_password):
                        print("You have a nice password.\n")
                        self.password = new_password
                        return
                    elif self.mid_passwd(new_password):
                        print("So so, but okey\n")
                        self.password = new_password
                        return
                    else:
                        print("Sorry, try more better password.\n")
                        cnt += 1
                        if cnt == 3:
                            print("Too many attempts, try again later.\n")
                            return

    def change_email(self):
        cnt = 0
        while True:
            email_check = str(input(f"{self.username}, write your new email: \n"))
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
                print("Too many attempts, try again later.\n")
                return

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
        answers = ["yes"]
        display_passwd = str(input("Do you want to see your passwd?\n"))
        new_answer = display_passwd.lower()
        cnt = 0
        if new_answer in answers:
            while True:
                email_check = str(input("Write your email to see your password:\n"))
                if email_check == self.email:
                    print(f"Ok. Here is your password: {self.password}\n")
                    break
                else:
                    print("It's not your email.\n")
                    cnt += 1
                if cnt == 3:
                    print("Too many attempts, try again later")


class Transaction:
    def __init__(self, amount, transaction_type, date, sender, receiver):
        self.amount = amount
        self.transaction_type = transaction_type
        self.date = date
        self.sender = sender
        self.receiver = receiver


class BankAccount(User):

    def __init__(self, owner, balance, username, email, password, number_of_bank_account):
        super().__init__(username, email, password)
        self.owner = owner
        self.balance = balance
        self.transactions = []
        self.number_of_bank_account = number_of_bank_account

    def display_account_info(self):
        print(f"Owner: {self.owner}")
        print(f"Username: {self.username}")
        print(f"You number of bank account: {self.number_of_bank_account}")
        print(f"Balance: {self.balance}$")

    def deposit(self, sum_of_moneys):
        self.balance += sum_of_moneys

    def withdraw(self, sum_of_moneys):
        self.balance -= sum_of_moneys

    def check_balance(self):
        print(f"{self.username} on your account {self.balance}$\n")

    def transfer(self, amount, dst):
        if amount < 0:
            print("Invalid amount\n")
            return
        elif self.balance < amount:
            print("Don't have enough money.\n")
            return
        if not isinstance(dst, BankAccount):
            print("Destination account does not exist.")
            return
        self.balance -= amount
        dst.deposit(amount)
        print(f"Successfully transferred {amount}$ to {dst.owner}'s account.")
        transaction = Transaction(amount, "transfer", datetime.now(), self.username, dst.username)
        self.transactions.append(transaction)
        dst_transaction = Transaction(amount, "transfer", datetime.now(), self.username, dst.username)
        dst.transactions.append(dst_transaction)

    def display_transactions(self):
        print(f"{self.owner} all transactions:\n")
        for transaction in self.transactions:
            print(f"Date: {transaction.date}, Type: {transaction.transaction_type}, Amount: {transaction.amount}$, "
                  f"Sender: {transaction.sender}, Receiver: {transaction.receiver}\n")
        print(f" Now you have {self.balance}$")


def create_user(username, email, password):
    return User(username, email, password)


def display_info_bank(account, username):
    answer = input(f"{username}, do you want to see your info? (yes/no): ").lower()
    if answer == "yes":
        account.display_account_info()


def create_bank_account(user):
    answers = ["yes"]
    display_passwd = str(input(f"{user.username}, do you want to create your bank account?"))
    new_answer = display_passwd.lower()
    if new_answer in answers:
        name = str(input("Write your name:"))
        answers = ["yes"]
        answer = str(input("Do you want to deposit some cash?"))
        new_answer = answer.lower()
        if new_answer in answers:
            money = float(input("How much money?\n"))
        else:
            money = 0
        number = random.randint(100000, 999999)
        return BankAccount(name, money, user.username, user.email, user.password, number), True
    else:
        print("Ok, bye\n")
        return None, False


if __name__ == '__main__':
    user1 = create_user("rayzqq", "asirbabayanvlad@gmail.com", "jsbxiq8")
    user2 = create_user("bambo", "bimba@yandex.ru", "nbhq81b")
    user3 = create_user("mindan", "minakov.danil@yahoo.com", "bdkqp")
    bank_account1, success1 = create_bank_account(user1)
    bank_account2, success2 = create_bank_account(user2)
    bank_account3, success3 = create_bank_account(user3)
    accounts = [(bank_account1, success1, user1.username), (bank_account2, success2, user2.username),
                (bank_account3, success3, user3.username)]
    for account, success, username in accounts:
        if success:
            while True:
                action = input(f"What do you want to do {username}?:\n"
                               f"1.Display info of your bank account.\n2.Do a transfer.\n"
                               "3.See all of your transactions.\n")
                if action == "1":
                    account.display_account_info()
                elif action == "2":
                    dst_num = int(input(f"To which account you want to transfer:\n"
                                       f"1.{user1.username}\n2.{user2.username}\n3.{user3.username}\n"))
                    dst_account = None
                    if dst_num == 1:
                        dst_account = bank_account1
                    elif dst_num == 2:
                        dst_account = bank_account2
                    elif dst_num == 3:
                        dst_account = bank_account3
                    if dst_account == account:
                        print("You can't transfer to yourself.\n")
                    else:
                        amount = int(input("Write the amount.\n"))
                        account.transfer(amount, dst_account)
                elif action == "3":
                    account.display_transactions()
                answer = input("This is all?\n").lower()
                if answer == 'yes':
                    break
                else:
                    pass
    user1.change_email()
    user2.change_password()
    user1.display_info()
    user2.display_info()
    user3.display_info()
