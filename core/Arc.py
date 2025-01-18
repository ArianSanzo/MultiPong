import pygame
import math
import json

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)

"""
Arc:
    - circle's center cartesian coordinates: x_center; y_center
    - circle radius: radius
    - start of the circle's segment (on radians, -pi to pi): starting_angle
    - ending of the circle's segment (on radians, -pi to pi): ending_angle
    - arc's width (for drawing): width
    - arc's resolution (points quantity): resolution
    - arc's color (RGB): color
    - arc's points (list of cartesian coordinates): points
    - arc's sprite (.png): sprite
"""


class Arc:
    def __init__(self, x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite,
                 color=(255, 255, 255)):
        self._x_center = x_center
        self._y_center = y_center
        self._radius = radius
        self._starting_angle = starting_angle  # On radians
        self._ending_angle = ending_angle  # On radians
        self._width = width
        self._resolution = resolution
        self._color = color  # RGB
        self._sprite = sprite
        self._points = self.generate_points()

    def x_center(self):
        return self._x_center

    def y_center(self):
        return self._y_center

    def radius(self):
        return self._radius

    def starting_angle(self):
        return self._starting_angle

    def ending_angle(self):
        return self._ending_angle

    # Generates the list of the arc´s points
    def generate_points(self):
        points = []
        for i in range(self._resolution + 1):
            t = i / self._resolution  # (0% to 100%)
            angle = self._starting_angle + t * (self._ending_angle - self._starting_angle)
            x = self._x_center + self._radius * math.cos(angle)
            y = self._y_center - self._radius * math.sin(angle)
            points.append((x, y, angle))
        return points

    # Draws the arc
    def draw(self, screen):
        if len(self._points) > 1:
            if config['retro']:
                x_y_only_list = []
                for point in self._points:
                    x, y, angle = point
                    x_y_only_list.append((x, y))
                pygame.draw.lines(screen, self._color, False, x_y_only_list, self._width)
            else:
                for point in self._points:
                    x, y, angle = point
                    rotated_sprite = pygame.transform.rotate(self._sprite, math.degrees(angle) - 90)
                    screen.blit(rotated_sprite, (x - self._sprite.get_width() // 2,
                                                 y - self._sprite.get_height() // 2))
