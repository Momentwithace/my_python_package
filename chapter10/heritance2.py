class Animal:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        print("I am barking")

class Dog(Animal):
    def __init__(self, name, breed, color="Brown"):
        super().__init__(name, breed)
        self.color = color

class Cat(Animal):
    pass
dog = Dog("Max", "Pug", "Brown")
dog.speak()
print(dog.name)
print(f"I'm a Dog, my name is {dog.name} i can {dog.speak()} i belong to the {dog.breed}'s family my skin color is {dog.color}")