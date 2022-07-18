from projects.twitter import json_handler
# from projects.twitter.user_profile import profile_menu

db = json_handler.read_mydata_base()
def view_profile(new_user: dict):
    for user in db:
        if user["user_name"] == signIn(new_user) and user["password"] == signIn(new_user):
            print(user)
    pass


def home(new_user: dict):
    pass


def search(new_user: dict):
    pass


def view_follower(new_user: dict):
    pass


def send_message(new_user: dict):
    pass


def profile_menu(new_user: dict):
    user_menu = int(input("""
    1 -> View Profile
    2 -> Home
    3 -> Search
    4 -> View Follower List
    5 -> Send Message
    0 -> Quit
    >>>"""))
    match user_menu:
        case 1:
            view_profile(new_user)
        case 2:
            home(new_user)
        case 3:
            search(new_user)
        case 4:
            view_follower(new_user)
        case 5:
            send_message(new_user)
        case 0:
            print("Goodbye")

def signIn(new_user: dict):
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    db = json_handler.read_mydata_base()
    initial_size = len(db)
    for user in db:
        if user["user_name"] == username and user["password"] == password:
            print(username.upper() + " log in successfully...")
            profile_menu(new_user)
            break
    if initial_size == len(db):
        print("Incorrect Username or Password")


def autoSignIn(username, password):
    db = json_handler.read_mydata_base()
    for user in db:

        if user["user_name"] == username and user["password"] == password:
            print(username.upper() + " Logged in successfully")
            profile_menu()
            break
        else:
            print("Incorrect details Username or Password")

