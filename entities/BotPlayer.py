from entities.Player import Player
from entities.PlayerGoal import PlayerGoal
from entities.Ball import Ball
import math
import json
from utils.math_utils import normalize_angle

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)


class BotPlayer(Player):
    def __init__(self, x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite,
                 color=(255, 255, 255), speed=(config['player_speed'])):
        super().__init__(x_center, y_center, radius, starting_angle, ending_angle, width, resolution, sprite,
                         color, speed)

    def mid_angle(self):
        return super().mid_angle()

    def move(self, goal: PlayerGoal):
        super().move(goal)
    
    def rotates_clockwise(self):
        super().rotates_clockwise()
        
    def not_rotates_clockwise(self):
        super().not_rotates_clockwise()
    
    def rotates_counterclockwise(self):
        super().rotates_counterclockwise()
    
    def not_rotates_counterclockwise(self):
        super().not_rotates_counterclockwise()

    def chase_ball(self, ball: Ball, goal: PlayerGoal):
        mid_angle = self.mid_angle()
        if goal.starting_angle() < goal.ending_angle():
            if ball.angle_from_center() < mid_angle:
                self.rotates_clockwise()
                self.not_rotates_counterclockwise()
            else:
                self.rotates_counterclockwise()
                self.not_rotates_clockwise()
        else:
            print(self.mid_angle(), ball.angle_from_center())
            if (self.mid_angle() < 0 and ball.angle_from_center() < 0) or (self.mid_angle() > 0 and ball.angle_from_center() > 0):
                if ball.angle_from_center() < mid_angle:
                    self.not_rotates_counterclockwise()
                    self.rotates_clockwise()
                else:
                    self.not_rotates_clockwise()
                    self.rotates_counterclockwise()
            else:
                if ball.angle_from_center() < mid_angle:
                    self.rotates_counterclockwise()
                    self.not_rotates_clockwise()
                else:
                    self.rotates_clockwise()
                    self.not_rotates_counterclockwise()
