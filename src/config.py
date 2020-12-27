import json


class Config(object):
    def __init__(self):
        self.CONFIG_LOCATION = './config.json'

    def load_config(self):
        with open(self.CONFIG_LOCATION) as f:
            return json.load(f)