name = input("what is your name: ")
if name != name.upper():
    print("your name must be in capital letters!!!")
    input("what is your name: ")
    if name == name.upper():
        print(name)
else:
    print("what is your name: ")