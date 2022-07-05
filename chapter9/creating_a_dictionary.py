# creating a new dictionary
captains = {}

# adding keys and values to the element in a dictionary
captains["Enterprise"] = "Picard"
captains["Voyager"] = "Janeway"
captains["Defiant"] = "Sisko"


# accessing the elements in the dictionary
if "Enterprise" in captains:
    print(f"The Captain of Enterprise is {captains['Enterprise']}.")
else:
    print("unknown")

if "Discovery" in captains:
    print(f"\nThe Captain of Discovery is {captains['Discover']}")
else:
    print("Unknown")


# using for loop to display all the element in the dictionary
# with their keys and values

for ships in captains:
    print(f"The Captain of this {ships} is {captains[ships]}")

print()

captains = dict({"Enterprise": "Picard", "Voyager": "Janeway", "Defiant": "Sisko"})
for ship, captains in captains.items():
    print(f"The Captain of {ship} is {captains}")
