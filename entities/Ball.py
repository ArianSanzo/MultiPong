import math
import pygame
from core.Arc import Arc
from entities.Player import Player
"""
Ball:
"""


class Ball:
    def __init__(self, x, y, radius, direction_angle, speed, color, sprite):
        self._x = x
        self._y = y
        self._radius = radius
        self._direction_angle = direction_angle
        self._speed = speed
        self._speed_components = self.speed_components()
        self._color = color
        self._sprite = sprite
        self._last_touch = None

    def speed_components(self):
        speed_x = self._speed * math.cos(self._direction_angle)
        speed_y = - self._speed * math.sin(self._direction_angle)
        return speed_x, speed_y

    def update_speed_components(self):
        self._speed_components = self.speed_components()

    def move(self, obj_list):
        for obj in obj_list:
            if isinstance(obj, Arc):

                obj_distance = math.sqrt((obj.x_center() - self._x) ** 2 + (obj.y_center() - self._y) ** 2)
                obj_and_ball_angle = math.atan2(-(obj.y_center() - self._y), obj.x_center() - self._x) - math.pi
                obj_and_ball_angle = ((obj_and_ball_angle + math.pi) % (2 * math.pi)) - math.pi
                angle_diff = abs(self._direction_angle - obj_and_ball_angle)

                if (obj.radius() - self._radius - 0 < obj_distance < obj.radius() + self._radius + 0 and
                        obj.starting_angle() < obj_and_ball_angle < obj.ending_angle()):
                    new_angle = self._direction_angle + math.pi
                    if self._direction_angle < obj_and_ball_angle:
                        new_angle += angle_diff * 2
                    else:
                        new_angle -= angle_diff * 2
                    new_angle = ((new_angle + math.pi) % (2 * math.pi)) - math.pi
                    self.change_direction_angle(new_angle)
                    self.update_speed_components()
                    if isinstance(obj, Player):
                        self._last_touch = obj.get_id()

        self._x += self._speed_components[0]
        self._y += self._speed_components[1]

    def change_direction_angle(self, angle):
        self._direction_angle = angle

    def draw(self, display):
        pygame.draw.circle(display, self._color, (self._x, self._y), self._radius)
