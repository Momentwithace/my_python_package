from projects.phoneBookApp.main import create_phoneBook, login_into_phoneBook, about_phoneBook


# def phonebook_page(user: dict):
#     user_input = int(input("""
#     ==================================
#      WELCOME TO ACE MOBILE PHONE-BOOK
#         1 -> Create Phone-Book
#         2 -> Login into Phone-Book
#         3 -> About us
#         4 -> Quit
#     ==================================
#     >>>"""))
#     match user_input:
#         case 1: create_phoneBook(user)
#         case 2: login_into_phoneBook()
#         case 3: about_phoneBook()
#         case _: print("GoodBye")
#     return user_input
#
# match phonebook_page({}):
#     case 1: create_phoneBook({})
#     case 2: login_into_phoneBook()
#     case 3: about_phoneBook()
#     case _: print("GoodBye")