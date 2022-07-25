class Person:
    def __init__(self, name: str) -> None:
        self.__name = name
        self._name = name
        self.__age = 17

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, new_name):
        if new_name < 0:
            raise ValueError("Age can not be negative")
        self._name = new_name

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Name will now be deleted")
        del self._name

    @name.setter
    def name(self, value):
        self._name = value

    @classmethod
    def get_number_of_persons(cls):
        return cls.get_number_of_persons

    @staticmethod
    def determine_class(age: int) -> str:
        if age >= 18:
            return "Major"
        return "Minor"


person1 = Person("Omotola")
person2 = Person("Dorcas")
print(person1.name)
person1.name = "Abigail"

del person1.name

print(person1.name)
print(dir(person1))
