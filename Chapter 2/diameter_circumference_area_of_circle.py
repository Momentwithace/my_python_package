print("Enter The radius of a circle")
print("to find the diameter, circumference and area")
number = int(input("Enter radius of circle: "))


diameter = 2 * number
print("Diameter is: " + str(diameter))

circumference = 2 * number * 3.14
print("Circumference is :" + str(circumference))

area = number * number * 3.14
print("Area is :" + str(area))