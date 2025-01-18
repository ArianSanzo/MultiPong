from entities.Player import Player
from entities.BotPlayer import BotPlayer


class PlayerFactory:
    @staticmethod
    def create_player(player_type):
        if player_type == "bot":
            pass
        elif player_type == "player":
            pass
