from core.Arc import Arc
import json

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)

"""
Player:
    - Player id (int): id
    - Average player speed: speed
    - If player is rotating clockwise (bool): rotates_clockwise
    - If player is rotating counterclockwise (bool): rotates_counterclockwise
    For more info look for Arc comments.
"""


class Player(Arc):
    id = 0

    def __init__(self, x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite,
                 color=(255, 255, 255), speed=(config['player_speed'])):
        Player.id += 1
        super().__init__(x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite, color)
        self._speed = speed
        self._rotates_clockwise = False
        self._rotates_counterclockwise = False
        self._id = Player.id

    def x_center(self):
        return super().x_center()

    def y_center(self):
        return super().y_center()

    def radius(self):
        return super().radius()

    def starting_angle(self):
        return super().starting_angle()

    def ending_angle(self):
        return super().ending_angle()

    def get_id(self):
        return self._id

    def draw(self, screen):
        super().draw(screen)
    