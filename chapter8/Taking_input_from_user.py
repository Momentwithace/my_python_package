for i in range(3):
    userInput = input("Enter Any Character: ")
    if userInput == 'q' or userInput == 'Q':
        print("Correct")
        break
    print("Wrong Input.")
else:
    print("Session Is Over!")