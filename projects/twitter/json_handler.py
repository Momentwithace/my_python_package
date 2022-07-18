import json
from pathlib import Path

mydata_base = Path.cwd() / "db.json"
mydata_base.touch()

# with mydata_base.open(mode="w", encoding="utf-8") as file:
#     json.dump([], file, indent=4)


def write_to_mydata_base(new_user: list) -> None:
    with mydata_base.open(mode="w", encoding="utf-8") as file:
        return json.dump(new_user, file, indent=4)


def read_mydata_base() -> list:
    with mydata_base.open(mode="r", encoding="utf-8") as file:
        return json.load(file)

def update_mydata_base(el) -> None:
    with mydata_base.open(mode="w", encoding="utf-8") as file:
        json.dump(el, file, sort_keys=True, indent=4)
