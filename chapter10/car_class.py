class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def description(self):
        return f"The {self.color} car has {self.mileage} miles"


blue = Car("blue", "20,000")
print(f"The {blue.color} car has {blue.mileage} miles")

red = Car("red", "30,000")
print(f"The {red.color} car has {red.mileage} miles")