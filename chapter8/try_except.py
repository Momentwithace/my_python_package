for i in range(5):
    try:
        user_input = int(input("Enter An Integer: "))
        print(user_input)
        break

    except ValueError:
        print("Try Again")

