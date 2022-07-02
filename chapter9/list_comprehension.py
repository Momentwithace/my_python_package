# list comprehension using a print statement
numbers = [2, 3, 5, 7, 9]
square = [num**2 for num in numbers]
print(square)

# list comprehension using print f
print(f"Square of {[2, 3, 5, 7, 9]} -> {[num**2 for num in numbers]}")