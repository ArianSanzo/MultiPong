import json


class Config:
    """Used only to create the config constant"""
    def __init__(self, file_name="data/config.json"):
        self._file_name = file_name
        self._data = {}
        self.load()

    def load(self):
        """Loads configs from a json"""
        try:
            with open(self._file_name, 'r') as f:
                self._data = json.load(f)
        except FileNotFoundError:
            print("Configurations file not found.")
            self._data = {}

    def data(self):
        return self._data


config = Config()
