print("Type help for game menu...")
player_command = " "
started = False
while True:
    player_command = input(">>>").lower()
    if player_command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Car started...")
    elif player_command == "stop":
        if not started:
            print("Car already stopped!!!")
        else:
            started = False
            print("Car stopped")
    elif player_command == "help":
        print("""
         start -> to start the car
         stop -> to stop the car
         quit -> to quit
        """)
    elif player_command == "quit":
        break
    else:
        print("Command Not Found")
