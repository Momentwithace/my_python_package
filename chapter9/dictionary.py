# creating a dictionary
# dictionary as to do with keys and values
# to access the element in a dictionary you need to use the key
capital = {"California": "Sacramento", "New York": "Albany",
           "Colorado": "Denver"}
# using for loop to access the element in the dictionary
for state in capital:
    print(f"The Capital of {state} is {capital[state]}")

# another way of looping through a dictionary using the .item function is
print()

for state, capital in capital.items():
    print(f"The Capital of {state} is {capital}")