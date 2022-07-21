import pathlib
import yaml


file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Ace', 'age': 16, 'children': ["Boyo", "Tman"]}
with file_path.open(mode="w") as new_file:
    yaml.dump(text, new_file, sort_keys=False)

with file_path.open(mode="r", encoding="utf-8") as file:
    text = yaml.load(file, Loader=yaml.Loader)

print(text)