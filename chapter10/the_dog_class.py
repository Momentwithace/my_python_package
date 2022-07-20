class Dog:
    species = "Canis Familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} year old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def color(self, coat_color):
        return f"{self.name}'s coat is {coat_color}"


philo = Dog("Philo", 5)
print(f"{philo.name} is {philo.age} year's old")