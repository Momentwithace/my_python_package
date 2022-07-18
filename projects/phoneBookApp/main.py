import re

phonebook_user_list = []


def phonebook_page(user: dict):
    user_input = int(input("""
    ==================================
     WELCOME TO ACE MOBILE PHONE-BOOK
        1 -> Create Phone-Book
        2 -> Login into Phone-Book
        3 -> About us
        4 -> Quit
    ==================================    
    >>>"""))
    match user_input:
        case 1:
            create_phoneBook(user)
        case 2:
            login_into_phoneBook({})
        case 3:
            about_phoneBook()
        case _:
            print("GoodBye")
    return user_input


def create_phoneBook(user: dict):
    user_id = 0
    unique_id = 1
    print("Fill-in Profile Details")
    user_id += unique_id + 1
    name = input("Enter Full-Name: ")
    while not name.isalpha():
        print("Name should be in character")
        print("Example: 'JOHN'")
        name = input("Enter Full-Name: ")
    gender = input("Enter Gender: ")
    age = input("Enter Age: ")
    while not age.isdigit():
        print("Age should be in digit")
        age = input("Enter Age: ")
    address = input("Enter Address: ")
    while len(address) < 0:
        address = input("Enter Address: ")
    phone_number = input("Enter Phone-Number: ")
    while not phone_number.isdigit():
        print("Phone-Number should be in digit")
        phone_number = input("Enter Phone-Number: ")
    while not phone_number.isdigit():
        phone_number = input("Enter Phone-Number: ")
    email = input("Enter E-mail: ")
    while email.endswith('@gmail.com' or '@yahoo.com' or '@hotmail.com' or '@outlook.com') is not True:
        print("Invalid Email-address")
        email = input("Enter Email-address: ")
    user_name = input("Enter User-Name: ")
    password = input("Enter Password: ")
    password_check = re.compile('[!@#$%^&*()_+=}{|?/.>,<]')
    while password_check.search(password) is None:
        print("Password too easy to guess")
        print("Include any special character")
        password = input("Create Password: ")
    while len(password) < 5:
        print("Password Too Short")
        password = input("Create Password: ")
    print("Account Successfully Created")
    print()
    print(f'Hello ' + user_name.upper() + ' your phone-book as been successfully created...')
    print("Your User-name is: " + user_name + '\nYour Password is : ' + password + '\nKeep your login details save.')
    new_user = {'Full_name': name,
                'Gender': gender,
                'Age': age,
                'Address': address,
                'Phone_number': phone_number,
                'Email': email,
                'User_name': user_name,
                'Password': password,
                'Contacts': []
                }
    phonebook_user_list.append(new_user)
    print()
    user_input = int(input("""
           1 -> Sign to continue using app
           0 -> Log-out
       >>>"""))
    match user_input:
        case 1:
            user_phone_book(new_user)
        case 0:
            print("GoodBye " + user_name)
    pass

    pass


def view_profile(new_user: dict):
    for k, v in new_user.items():
        if k != "Password":
            print(f"{k} -> {v}")

    user_phone_book(new_user)
    pass


def create_contact(new_user: dict):
    id = 0
    unique_id = 0
    id += unique_id + 1
    name = input("Enter Full-name: ")
    address = input("Enter Address: ")
    phone_number = input("Enter Phone-Number: ")
    email = input("Enter E-mail: ")
    print("Contact Added")
    contact = {'Contact-Id': id,
               'Full-Name': name,
               'Address': address,
               'Phone-Number': phone_number,
               'E-mail': email}
    new_user['Contacts'].append(contact)

    user_input = int(input("""
       1 -> view contact list
       2 -> add other contact
       0 -> back
       >>>"""))
    match user_input:
        case 1:
            for contact in new_user['Contacts']:
                print(contact)
            user_phone_book(new_user)
        case 2:
            create_contact(new_user)
        case 0:
            user_phone_book(new_user)
        case _:
            print("invalid input");
            user_phone_book(new_user)

    return new_user['Contacts']
    pass


def search_contact(new_user: dict):
    print("You can search for contact using contact name")
    contact_name = input("Enter Contact Name: ")
    initial_size = len(new_user['Contacts'])
    for user in new_user['Contacts']:
        if user["Full-Name"] == contact_name:
            print(user)
            break
        else:
            if initial_size == len(new_user['Contacts']):
                print("contact not found")
                print("these are your contacts")
                for contact in new_user['Contacts']:
                    print(contact)
        user_input = int(input("0 -> Back"))
        if user_input == 0:
            user_phone_book(new_user)
        else:
            print("invalid entry")
    phonebook_page(new_user)
    pass


def view_all_contact(new_user: dict):
    for contact in new_user['Contacts']:
        print(contact)
    user_phone_book(new_user)
    pass


def delete_contact(new_user: dict):
    print("You can delete a contact using contact name")
    contact_name = input("Enter Contact Name: ")
    initial_size = len(new_user['Contacts'])

    for contact in new_user['Contacts']:
        if contact['Full-Name'] == contact_name:
            new_user['Contacts'].remove(contact)
            print("successfully deleted")

    if initial_size == len(new_user['Contacts']):
        print("Contact not found")
        print("Contact List")
        for contact in new_user['Contacts']:
            print(contact)
        delete_contact(new_user)
    phonebook_page(new_user)


def user_phone_book(new_user: dict):
    user_input = int(input("""
    1 -> View Profile
    2 -> Create Contact
    3 -> Search Contact
    4 -> View All Contact
    5 -> Delete Contact
    6 -> Back
    0 -> Quit
    """))
    match user_input:
        case 1:
            view_profile(new_user)
        case 2:
            create_contact(new_user)
        case 3:
            search_contact(new_user)
        case 4:
            view_all_contact(new_user)
        case 5:
            delete_contact(new_user)
        case 6:
            phonebook_page(new_user)
        case 0:
            print("GoodBye")

    pass


def login_into_phoneBook(new_user: dict):
    user_name = input("Enter Username: ")
    password = input("Enter Password: ")
    user_ = None
    for user in phonebook_user_list:
        if user["User_name"] == user_name and user["Password"] == password:
            print(user_name.upper() + " log in successfully...")
            user_ = user
            user_phone_book(new_user)
            break
    if user_ is None:
        print("Incorrect Username or Password")
    phonebook_page(new_user)

    pass


def about_phoneBook():
    print("Mobile Phone-Book is just an online contact saver")
    phonebook_page({})
    pass


match phonebook_page({}):
    case 1:
        create_phoneBook({})
    case 2:
        login_into_phoneBook({})
    case 3:
        about_phoneBook()
    case _:
        print("GoodBye")
