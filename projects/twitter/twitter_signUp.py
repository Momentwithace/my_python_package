import string
import re
import json_handler
from twitter_signIn import autoSignIn


def signUp(new_user: dict):
    first_name = input("Enter First-name: ")
    while not first_name.isalpha():
        print("Name should be in character")
        print("Example: 'JOHN'")
        first_name = input("Enter First-name: ")
    second_name = input("Enter Second-name: ")
    while not second_name.isalpha():
        print("Name should be in character")
        print("Example: 'JOHN'")
        second_name = input("Enter Second-name: ")
    gender = input("Enter Gender: ")
    age = input("Enter Age: ")
    while not age.isdigit():
        print("Age should be in digit")
        age = input("Enter Age: ")
    location = input("Enter Location: ")
    sign_up_option = int(input("""
                1 -> Sign-Up with Email-Address
                2 -> Sign-up with Phone-Number

                >>>"""))
    if sign_up_option == 1:
        email_address = input("Enter Email-address: ")
        while email_address.endswith('@gmail.com' or '@yahoo.com' or '@hotmail.com' or '@outlook.com') is not True:
            print("Invalid Email-address")
            email_address = input("Enter Email-address: ")
        else:
            print("A verification code as been send to your Email")
    if sign_up_option == 2:
        phone_number = input("Enter Phone-number: ")
        while not phone_number.isdigit():
            print("Invalid Phone")
            phone_number = input("Enter a valid phone-number: ")
        while len(phone_number) != 11:
            print("Invalid")
            phone_number = input("Enter a valid phone-number: ")
    user_name = input("Enter User-Name: ")
    password = input("Create Password: ")
    string_check = re.compile('[!@#$%^&*()_+=}{|?/.>,<]')
    while string_check.search(password) is None:
        print("Password too easy to guess")
        print("Include any special character")
        password = input("Create Password: ")
    while len(password) < 5:
        print("Password Too Short")
        password = input("Create Password: ")
    print("Account Successfully Created")
    print()
    print(f'Hello ' + user_name.upper() + ' your account as been successfully created...')
    print("Your User-name is : " + user_name + '\nYour Password is : ' + password + '\nKeep your login details save...')
    print()
    user_input = int(input("""
     1 -> Sign to continue using app
     0 -> Quit app
     >>>"""))
    match user_input:
        case 1:
            autoSignIn(user_name, password)
        case 2:
            print(f'' + user_name.upper() + ' GoodBye')

    new_user = {'first_name': first_name,
                'second_name': second_name,
                'gender': gender,
                'age': age,
                'location': location,
                'sign_up_option': sign_up_option,
                'user_name': user_name,
                'password': password,
                'followers': [],
                'following': []
                }
    old_db: list = json_handler.read_mydata_base()
    new_db = old_db.append(new_user)
    json_handler.write_to_mydata_base(old_db)

    # autoSignIn(user_name, password)

    pass
