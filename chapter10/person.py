class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


ace = Person("Black Ace")
ace.talk()

pat = Person("Little Pat")
pat.talk()