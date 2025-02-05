import math
import pygame
import random
from core.Arc import Arc
from entities.Player import Player
from entities.PlayerGoal import PlayerGoal
import utils.math_utils as m_utils
from data.config import config as cnfg

# Loading configurations
config = cnfg.data()


class Ball:
    """
    Ball:
        - ball's center cartesian coordinates: (x; y)
        - ball's radius: radius
        - ball's direction's angle (radians): direction_angle
        - ball's speed: speed
        - ball's speed components (speed on x and y) obtained from speed and direction_angle
        - ball's color (RGB): color
        - ball's sprite (.png): sprite
        - last touched by a Player object
    """
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

    # With cosine and sine the speeds components are obtained
    def speed_components(self):
        speed_x = self._speed * math.cos(self._direction_angle)
        speed_y = - self._speed * math.sin(self._direction_angle)
        return speed_x, speed_y

    def update_speed_components(self):
        self._speed_components = self.speed_components()

    def reset(self):
        """Resets the ball to the center of the screen, the last touch and its speed"""
        self._x = config['screen_width'] / 2
        self._y = config['screen_height'] / 2
        self._speed = config['ball_speed']
        self.update_speed_components()
        self._last_touch = None

    def angle_from_center(self):
        """Calculates the angle between the ball and the center of the screen"""
        angle_from_center = math.atan2(-(config['screen_height']/2 - self._y),
                                       config['screen_width'] / 2 - self._x) - math.pi

        # Normalizes angle between -pi and pi
        angle_from_center = m_utils.normalize_angle(angle_from_center)

        return angle_from_center

    def move(self, obj_list):
        """Moves the position of the ball (updating x and y) depending on the collisions"""
        for obj in obj_list:
            if isinstance(obj, Arc):

                # Calculates the distance between the ball and the object's center with Pitagora's theorem
                obj_distance = math.sqrt((obj.x_center() - self._x) ** 2 + (obj.y_center() - self._y) ** 2)

                # Calculates the angle between the ball and the object's center with arctangent
                obj_and_ball_angle = math.atan2(-(obj.y_center() - self._y), obj.x_center() - self._x) - math.pi

                # Normalizes angle between -pi and pi
                obj_and_ball_angle = m_utils.normalize_angle(obj_and_ball_angle)

                # Difference between the speed direction angle and the angle between the ball and the object's center
                angle_diff = abs(self._direction_angle - obj_and_ball_angle)

                # If the ball is colliding with the object radius and is between it's starting and ending angles
                # Starting angle is smaller than ending angle
                case_one = (obj.starting_angle() < obj.ending_angle() and
                            obj.starting_angle() < obj_and_ball_angle < obj.ending_angle())
                # Ending angle is smaller than starting angle
                case_two = (obj.starting_angle() > obj.ending_angle() and
                            (obj.starting_angle() < obj_and_ball_angle <= math.pi or
                             -math.pi < obj_and_ball_angle < obj.ending_angle()))
                inside_radius = obj.radius() - self._radius < obj_distance < obj.radius() + self._radius

                if (case_one or case_two) and inside_radius:
                    # Reflects the angle on 180 grades (pi)
                    if angle_diff > 0.01:
                        new_angle = self._direction_angle + math.pi
                    else:
                        new_angle = self._direction_angle + math.pi * 3 / 4

                    # Adds the angle difference to give it a more natural collision
                    if self._direction_angle < obj_and_ball_angle:
                        new_angle += angle_diff * random.uniform(1.7, 2.3)
                    else:
                        new_angle -= angle_diff * random.uniform(1.7, 2.3)

                    # Changes the ball's speed angle and updates speed's components
                    self.change_direction_angle(new_angle)
                    self.update_speed_components()
                    self._speed += 1.01
                    self._x += self._speed_components[0] * 1.3
                    self._y += self._speed_components[1] * 1.3

                    # Saves the last player that touched the ball
                    if isinstance(obj, Player):
                        self._last_touch = obj

                    if isinstance(obj, PlayerGoal):
                        if self._last_touch:
                            if self._last_touch == obj.get_player():
                                self._last_touch.discount_goal()
                            else:
                                self._last_touch.score_goal()
                        else:
                            obj.get_player().discount_goal()
                        self.reset()

        # Updates ball's position
        self._x += self._speed_components[0]
        self._y += self._speed_components[1]

    def change_direction_angle(self, angle):
        new_angle = m_utils.normalize_angle(angle)
        self._direction_angle = new_angle

    def draw(self, display):
        """Draws the ball on a screen"""
        pygame.draw.circle(display, self._color, (self._x, self._y), self._radius)
