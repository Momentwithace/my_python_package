class Person:
    def __init__(self, name: str) -> None:
        self.name = name


person1 = Person("Ace")
print(person1.name)

# name mangling
print(person1.__dict__)