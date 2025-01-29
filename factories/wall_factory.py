from environment.Wall import Wall
import math
import json
from random import randint

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)


class WallFactory:
    @staticmethod
    def create_wall():
        return Wall(config['screen_width'] / 2 + randint(-300, 300),  config['screen_height'] / 2 - randint(-300, 300),
                    randint(25, 100),
                    -math.pi, math.pi, config['main_wall_width'], config['main_wall_resolution'], "")
