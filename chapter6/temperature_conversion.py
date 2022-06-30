def fahrenheit(degree_in_f):
    c = (degree_in_f - 32) * 5/9

    return c

result1 = fahrenheit(72)
print(f" is {result1:.2f} Degrees C")

def celsius(degree_in_c):
    f = (degree_in_c * 1.8) + 32

    return f

result = celsius(37)
print(f" is {result:.2f} Degrees f")


fahrenheit_ = int(input("Enter a temperature in degree f: "))
result1 = fahrenheit(fahrenheit_)
print(f"{fahrenheit_} degree f = {result1:.2f} Degrees C")

celsius_ = int(input("Enter a temperature in degree c: "))
result = celsius(celsius_)
print(f"{celsius_} degree c = {result:.2f} Degree F")