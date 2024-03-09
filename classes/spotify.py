import re


class User:
    usernames = []

    def __init__(self, username, password, email, subscribe):
        self.username = username
        self.password = password
        self.email = email
        self.subscribe = subscribe
        User.usernames.append(username)

    def subscribe(self):
        answer = input("Do you want to buy subscribe?\n").lower()
        if answer == "yes":
            self.subscribe = True
        else:
            self.subscribe = False

    def display_info(self):
        print(f"Username:{self.username}")
        print(f"Email: {self.email}")
        print(f"Subscribe: {self.subscribe}")
        answer = input("Do you want to see your password?\n").lower()
        if answer == "yes":
            cnt = 0
            while cnt != 3:
                email = input("Enter your email for that.\n")
                if check_email(email):
                    if email == self.email:
                        print(f"Password: {self.password}")
                        break
                    else:
                        print("It's not your email.\n")
                        break
                else:
                    if cnt + 1 == 3:
                        print("Try again later.")
                    print("Invalid email. Try again.\n")
                    cnt += 1


class Music:

    def __init__(self, name, artist, album, listeners, length):
        self.name = name
        self.artist = artist
        self.album = album
        self.listeners = listeners
        self.length = length

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Artist:{self.artist}")
        print(f"Album:{self.album}")
        print(f"Listeners:{self.listeners}")
        print(f"Length:{self.length}")


class Playlist(Music, User):

    def __init__(self, name_of_playlist, artist, name, album, listeners, length):
        super().__init__(name, artist, album, listeners, length)
        self.name_of_playlist = name_of_playlist


class Favourite(Music, User):

    def __init__(self, name, artist, album, listeners, length):
        super().__init__(name, artist, album, listeners, length)


def add_music():
    num_songs = int(input("How many songs do you want to add?\n"))
    songs = []
    for i in range(num_songs):
        print(f"\nEnter details for song {i+1}:\n")
        name = input("Enter the name of the song:\n")
        artist = input("Enter the name of the artist:\n")
        album = input("Enter the name of the album:\n")
        listeners = int(input("Enter the count of listeners per month:\n"))
        length = input("Enter the length of song in minutes and seconds (m:s):\n")
        song = Music(name, artist, album, listeners, length)
        songs.append(song)
    return songs


def check_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


def check_password(password):
    length = len(password)
    lettersu = any(c.isupper() for c in password)
    lettersl = any(c.islower() for c in password)
    digits = any(c.isdigit() for c in password)
    special_chars = "#@$!%"
    special = any(c in special_chars for c in password)
    if length < 8:
        print("It's too short.\n")
        return False
    elif lettersl and digits and not lettersu:
        print("You need to use uppercase letters\n")
        return False
    elif lettersu and digits and lettersl and not special:
        print("It's ok.\n")
        return True
    elif lettersu and digits and lettersl and special:
        print("It's very good.\n")
        return True


def check_username(username):
    for i in User.usernames:
        if username == i:
            print("You can't use this username.\n")
            return False
        else:
            return True
    return True


def create_user():
    print("Hi, it's your lovely Spotify, i see you want to register.\n")
    cnt = 0
    email = ''
    while True or cnt != 3:
        email = input("Enter your email address:\n")
        if check_email(email):
            print("Fine, now you need to create password.\n")
            break
        else:
            print("Your email address is not valid.\n")
            cnt += 1
    password = ''
    while True:
        password = input("Enter your password(the best password with A-z,0-9 and #@$!%):\n")
        if check_password(password):
            break
        else:
            print("Try again.\n")
    while True:
        username = input("Enter your username(you can use only A-z, digits and -,_):\n")
        if check_username(username):
            print("Very nice, you have ended your registration.\n")
            break
        else:
            print("Try again.\n")
    answer = input("Do you want to buy subscribe?\n").lower()
    if answer == "yes":
        subscribe = True
    else:
        subscribe = False
    return User(username, password, email, subscribe)


if __name__ == "__main__":
    user1 = create_user()
    user1.display_info()
    songs = add_music()
    for song in songs:
        song.display_info()
