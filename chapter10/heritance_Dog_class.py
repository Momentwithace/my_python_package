class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} year old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f'{self.name} says {sound}'


jack = Dog("jack", 5)
print(f"{jack.name} is {jack.age} year's old")

brown = GoldenRetriever("brown", 5)
print(f"{brown.name} is {brown.age} years old")