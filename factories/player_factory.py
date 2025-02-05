from entities.Player import Player
from entities.PlayerGoal import PlayerGoal
from data.config import config as cnfg
import math
from entities.BotPlayer import BotPlayer

# Loading configurations
config = cnfg.data()


class PlayerFactory:
    @staticmethod
    def create_player(players_quantity, bots_quantity):
        players = []
        goals = []
        total = players_quantity + bots_quantity
        if True:
            for i in range(players_quantity):
                mid_angle = 2 * math.pi * i / total
                distance_mid_angle = 1 / total
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
        if True:
            for i in range(players_quantity, total):
                mid_angle = 2 * math.pi * i / total
                distance_mid_angle = 1 / total
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
