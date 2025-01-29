from entities.Player import Player
from entities.PlayerGoal import PlayerGoal
import json
import math
from entities.BotPlayer import BotPlayer

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)


class PlayerFactory:
    @staticmethod
    def create_player(player_type, quantity):
        players = []
        goals = []
        if player_type == 'player':
            for i in range(quantity):
                mid_angle = 2 * math.pi * i / quantity
                distance_mid_angle = 1 / quantity
                goal_length = distance_mid_angle * 2
                player = Player(
                    config['screen_width'] / 2, config['screen_height'] / 2,
                    config['screen_height'] / 2 + config['player_radius'],
                    mid_angle - distance_mid_angle, mid_angle + distance_mid_angle,
                    config['main_wall_width'], 20, '', (100, 2, 100)
                )
                goal = PlayerGoal(
                    config['screen_width'] / 2, config['screen_height'] / 2,
                    config['screen_height'] / 2 + config['player_radius'] + 20,
                    mid_angle - distance_mid_angle - goal_length, mid_angle + distance_mid_angle + goal_length,
                    config['main_wall_width'], 20, '',
                    player
                )
                players.append(player)
                goals.append(goal)
        elif player_type == "bot":
            for i in range(quantity):
                mid_angle = 2 * math.pi * i / quantity
                distance_mid_angle = 1 / quantity
                goal_length = distance_mid_angle * 2
                player = BotPlayer(
                    config['screen_width'] / 2, config['screen_height'] / 2,
                    config['screen_height'] / 2 + config['player_radius'],
                    mid_angle - distance_mid_angle, mid_angle + distance_mid_angle,
                    config['main_wall_width'], 20, '', (100, 2, 100)
                )
                goal = PlayerGoal(
                    config['screen_width'] / 2, config['screen_height'] / 2,
                    config['screen_height'] / 2 + config['player_radius'] + 20,
                    mid_angle - distance_mid_angle - goal_length, mid_angle + distance_mid_angle + goal_length,
                    config['main_wall_width'], 20, '',
                    player
                )
                players.append(player)
                goals.append(goal)

        return players, goals
