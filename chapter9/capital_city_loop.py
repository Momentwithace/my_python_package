import random

capital_dict = {
    'Abia': 'Umuahia',
    'Adamawa': 'Yola',
    'Akwa-Ibom': 'Calabar',
    'Anambra': 'Awka',
    'Bauchi': 'Bauchi',
    'Bayelsa': 'Yenagoa',
    'Benue': 'Makurdi',
    'Borno': 'Maiduguri',
    'Cross-River': 'Calabar',
    'Delta': 'Asaba',
    'Ebonyi': 'Abakaliki',
    'Edo': 'Benin',
    'Ekiti': 'Ado-Ekiti',
    'Enugu': 'Enugu',
    'Gombe': 'Gombe',
    'Imo': 'Owerri',
    'Jigawa': 'Dutse',
    'Kaduna': 'Kaduna',
    'Kano': 'Kano',
    'Katsina': 'Kasina',
    'Kebbi': 'Benin kebbi',
    'Kogi': 'Lokoga',
    'Kwara': 'Ilorin',
    'Lagos': 'Ikeja',
    'Nasarawa': 'Lafia',
    'Niger': 'Minna',
    'Ogun': 'Abeokuta',
    'Ondo': 'Akure',
    'Osun': 'Oshogbo',
    'Ibadan': 'Oyo',
    'Plateau': 'Jos',
    'Rivers': 'Port Harcourt',
    'Sokoto': 'Sokoto',
    'Taraba': 'Jalingo',
    'Yobe': 'Damaturu',
    'Zamfara': 'Gusau',
    'Abuja': 'FCT',
}

# using for loop to display the keys and their values
for state, capital in capital_dict.items():
    print(f"The Capital of this {state} is {capital}")
print()

state, capital = random.choice(list(capital_dict.items()))
print("Type the word exit to quit the game")
while True:
    userInput = input(f"What's the Capital of {state}? ").lower()
    if userInput == "exit":
        print(f"The capital of '{state}' is '{capital}'.")
        print("Goodbye")
        break
    elif userInput == capital.lower():
        print("Correct! You Got It...")
        break
