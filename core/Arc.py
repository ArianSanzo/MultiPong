import pygame
import math
from data.config import config as cnfg
import utils.math_utils as m_utils

# Loading configurations
config = cnfg.data()


class Arc:
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
    def __init__(self, x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite,
                 color=(255, 255, 255)):
        self._x_center = x_center
        self._y_center = y_center
        self._radius = radius
        starting_angle_normalized = m_utils.normalize_angle(starting_angle)
        self._starting_angle = starting_angle_normalized  # On radians
        ending_angle_normalized = m_utils.normalize_angle(ending_angle)
        self._ending_angle = ending_angle_normalized  # On radians
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

    def generate_points_in_range(self, resolution, starting_angle, ending_angle):
        """Generates 'resolution' number of points from the starting_angle to the ending_angle"""
        points = []
        for i in range(math.floor(resolution + 1)):
            t = i / resolution  # (0% to 100%)
            angle = starting_angle + t * (ending_angle - starting_angle)
            angle = m_utils.normalize_angle(angle)
            x = self._x_center + self._radius * math.cos(angle)
            y = self._y_center - self._radius * math.sin(angle)
            points.append((x, y, angle))
        return points

    def generate_points(self):
        """Calls to generate_points_in_range checking the order of the angles first"""
        if self._starting_angle < self._ending_angle:
            points = self.generate_points_in_range(self._resolution, self.starting_angle(), self.ending_angle())
        else:
            points = self.generate_points_in_range(self._resolution / 2, self.starting_angle(), math.pi)
            points += self.generate_points_in_range(self._resolution / 2, -math.pi, self.ending_angle())
        return points

    def draw(self, screen):
        """Draws the arc on a screen drawing point by point"""
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
