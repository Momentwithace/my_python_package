from projects.twitter import json_handler
from projects.twitter.twitter_signIn import signIn
from projects.twitter.twitter_signUp import signUp


def menu_page():
    prompt = int(input("""
    
            TWITTER
    
        1 -> Sign-Up
        2 -> Sign-In
        3 -> Adim Portal
        0 -> Quit
    
    >>>"""))
    return prompt


def admin_menu():
    command = int(input("""
         WELCOME TO ADMIN PORTAL
          1 -> View User
          2 -> Remove User
          3 -> Verify User 
          4 -> Block User 
          5 -> Previous Page
          >>>"""))

    def view_user():
        print("""
                 LIST OF TWITTER USER
            """)

        db = json_handler.read_mydata_base()
        for username in db:
            print(username)

        pass

    def remove_user():
        print("""
                    TO REMOVE AN ACCOUNT ENTER THE USER-NAME 
                    """)
        username = input("Enter User-name: ")
        db = json_handler.read_mydata_base()
        previous_length = len(db)
        for element in db:
            if username == element['user_name']:
                db.remove(element)
                print("User Successfully removed")
                break
        if previous_length == len(db):
            print("invalid username")
            return
        json_handler.update_mydata_base(db)
        user_input = int(input("""
            1 -> Press Y/y to go back to previous
            2 ->Press N/n to quit app
            >>>"""))
        if user_input == 1:
            admin_menu()
        elif user_input == 2:
            menu_page()
        else:
            print("Invalid Entry")

    def verify_user():

        pass

    def block_user():
        print("""
                                LIST OF TWITTER USER
                           """)

        db = json_handler.read_mydata_base()
        for username in db:
            print(["user_name"], username)
        print()
        account = input("To Block an Account Enter Account User-name: ")
        db = json_handler.read_mydata_base()
        for element in db:
            if account == element['user-name']:
                pass
        pass

    match command:
        case 1:
            view_user()

        case 2:
            remove_user()

        case 3:
            verify_user()

        case 4:
            block_user()

        case 5:
            menu_page()

    pass


match menu_page():
    case 1:
        signUp({})
    case 2:
        signIn()
    case 3:
        admin_menu()
    case 4:
        print("Goodbye")

#
# def admin_menu():
#     command = int(input("""
#      WELCOME TO ADMIN PORTAL
#       1 -> View User
#       2 -> Remove User
#       3 -> Verify User
#       4 -> Block User
#       5 -> Previous Page
#       >>>"""))
#
#     def view_user():
#         print("""
#              LIST OF TWITTER USER
#         """)
#
#         db = json_handler.read_mydata_base()
#         for username in db:
#             print(["user_name"], username)
#
#         pass
#
#     def remove_user():
#         print("""
#         TO REMOVE AN ACCOUNT ENTER THE USER-NAME
#         """)
#         username = input("Enter User-name: ")
#         db = json_handler.read_mydata_base()
#         for user in db:
#             if user["user_name"] == username:
#                 json_handler.read_mydata_base().remove(username)
#                 print("User Successfully removed")
#                 user_input = int(input("""
#                 1 -> Press Y/y to go back to previous
#                 2 ->Press N/n to quit app
#                 >>>"""))
#                 if user_input == 1:
#                     menu_page()
#                 elif user_input == 2:
#                     pass
#                 else:
#                     print("Invalid Entry")
#
#     def verify_user():
#         pass
#
#     def block_user():
#         pass
#
#     match command:
#         case 1:
#             view_user()
#
#         case 2:
#             remove_user()
#
#         case 3:
#             verify_user()
#
#         case 4:
#             block_user()
#
#         case 5:
#             menu_page()
