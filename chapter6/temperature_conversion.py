input_count = 0
while input_count <= 3:
    temp = int(input("Enter Temperature: "))
    user_input = int(input("""
        Enter Temperature to convert To.
         1 -> Convert To fahrenheit
         2 -> Convert To Celsius
        >>>"""))
    input_count = input_count + 1
    if user_input == 1:
        fahrenheit = (temp * 1.8) + 32
        print(f"Your Temperature is: " + str(fahrenheit) + " degree f")

    elif user_input == 2:
        celsius = (temp - 32) * 5 / 9
        print(f"Your Temperature is: " + str(celsius) + " degree c")

    else:
        print("Invalid Entry")

