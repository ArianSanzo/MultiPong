from core.Arc import Arc
from entities.PlayerGoal import PlayerGoal
import json
import math
import utils.math_utils as m_utils

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)

"""
Player:
    - Player id (int): id
    - Average player speed (radians): speed
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
        self._score = 0

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

    def mid_angle(self):
        if self.starting_angle() < self.ending_angle():
            mid_angle = self.starting_angle() + (self.ending_angle() - self.starting_angle()) / 2
        else:
            ending_angle = self.ending_angle() + 2 * math.pi
            mid_angle = self.starting_angle() + (ending_angle - self.starting_angle()) / 2
            mid_angle = m_utils.normalize_angle(mid_angle)
        return mid_angle

    # Rotates the player clockwise or anticlockwise
    def move(self, goal: PlayerGoal):
        if goal.starting_angle() < goal.ending_angle():
            if self.starting_angle() > goal.starting_angle() and self.ending_angle() < goal.ending_angle():
                if self._rotates_clockwise:
                    self._starting_angle -= self._speed
                    self._ending_angle -= self._speed
                if self._rotates_counterclockwise:
                    self._starting_angle += self._speed
                    self._ending_angle += self._speed

            if self.starting_angle() < goal.starting_angle():
                self._starting_angle += self._speed
                self._ending_angle += self._speed
            if self.ending_angle() > goal.ending_angle():
                self._starting_angle -= self._speed
                self._ending_angle -= self._speed
        else:
            condition_1 = self.starting_angle() > goal.starting_angle() or self.starting_angle() < 0
            condition_2 = self.ending_angle() < goal.ending_angle() or self.ending_angle() > 0
            if condition_1 and condition_2:
                if self._rotates_clockwise:
                    self._starting_angle -= self._speed
                    self._ending_angle -= self._speed
                if self._rotates_counterclockwise:
                    self._starting_angle += self._speed
                    self._ending_angle += self._speed

            if not condition_1 and condition_2:
                self._starting_angle += self._speed
                self._ending_angle += self._speed
            if condition_1 and not condition_2:
                self._starting_angle -= self._speed
                self._ending_angle -= self._speed

        if - math.pi > self.starting_angle() or self.starting_angle() > math.pi:
            self._starting_angle = m_utils.normalize_angle(self.starting_angle())
        if - math.pi > self.ending_angle() or self.ending_angle() > math.pi:
            self._ending_angle = m_utils.normalize_angle(self.ending_angle())

        self._points = self.generate_points()

    def score_goal(self):
        self._score += 1

    def discount_goal(self):
        self._score -= 1

    def get_score(self):
        return self._score

    def rotates_clockwise(self):
        self._rotates_clockwise = True

    def not_rotates_clockwise(self):
        self._rotates_clockwise = False

    def rotates_counterclockwise(self):
        self._rotates_counterclockwise = True

    def not_rotates_counterclockwise(self):
        self._rotates_counterclockwise = False
