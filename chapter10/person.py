class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"Hi, I am {self.name} and i'm {self.age}")


ace = Person("Black Ace", 5)
ace.talk()

pat = Person("Little Pat", 7)
pat.talk()