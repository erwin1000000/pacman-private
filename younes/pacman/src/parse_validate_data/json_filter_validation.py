from pathlib import Path
import json
from src.parse_validate_data.data_container import Data


class FilterValidateExtract:
    def __init__(self, path: Path):
        self.path = path

    def _filter(self):
        try:
            text = ""
            with self.path.open('r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith(('#', '//')):
                        pass
                    else:
                        text += line
            return text
        except FileNotFoundError:
            print(f"Error: {self.path.name} does not exit")

        except PermissionError:
            print(f"Error: you do not have the permission to read {self.path.name}")
            

    def _validate(self, text):
        dic = {}
        try:
            dic = json.loads(text)
        except json.JSONDecodeError:
            print("Error: the config file is not valid json")
        return dic
            

    def prossess(self):
        text = self._filter()
        dic = self._validate(text)
        data = Data(**dic)
        return data


        
