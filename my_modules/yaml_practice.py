import pathlib
import yaml


file_path = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Ace', 'age': 16, 'children': ["Boyo", "Tman"]}
with file_path.open(mode="w") as new_file:
    yaml.dump(text, new_file)