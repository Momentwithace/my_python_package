class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    @property
    def name(self):
        print("you're calling my name")
        return self._name

    @name.setter
    def name(self, name):
        print("setter")
        if "f" in name:
            print("Name Not accepted")
            return
        self._name = name


person1 = Person("Ace")
print(person1.name)


# name mangling
print(person1.__dict__)

person1.name = 'faith'
print(person1.name)