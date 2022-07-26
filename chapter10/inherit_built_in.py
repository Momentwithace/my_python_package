from enum import Enum, auto
from dataclasses import dataclass, field


class AgeGroup(Enum):
    # KID = auto()
    #
    # ADOLESCENT = auto()
    #
    # ADULT = auto()

    KID = "kid"

    ADOLESCENT = "teenager"

    ADULT = "adult"


@dataclass(order=True)
class Human:
    sort_by: tuple[int, str] = field(init=False, repr=False)
    name: str = "ace"
    age: int = 34
    gender: str = "male"
    children: list[str] = field(default_factory=lambda: [], init=False, repr=False)

    def __post_init__(self):
        self.sort_by = (self.age, self.name)

human = Human("Olalade", 25, "f")
alien = Human("Boyo", 45, "m")

print(human < alien)
human = Human()
print(human)

print(AgeGroup.KID.value)