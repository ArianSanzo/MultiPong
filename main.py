import math
import pygame
from entities.Player import Player
from entities.PlayerGoal import PlayerGoal
from entities.BotPlayer import BotPlayer
from environment.Wall import Wall
from entities.Ball import Ball
from factories.wall_factory import WallFactory
from factories.player_factory import PlayerFactory
from itertools import zip_longest
from data.config import config as cnfg

# Loading configurations
config = cnfg.data()


# Getting keys for players
keys_groups = []
for keys in config['player_movement_configs']:
    keys_groups.append((keys[0]['key_code'], keys[1]['key_code']))

# Pygame initialized
pygame.init()

# Screen
screen = pygame.display.set_mode((config['screen_width'], config['screen_height']))

# Game Caption
pygame.display.set_caption("MultiPong")

# Main Wall
wall_img = pygame.image.load(f"assests//images//environment//walls//wall_sprite.png")
main_wall = Wall(config['screen_width'] / 2,  config['screen_height'] / 2,
                 config['screen_height'] / 2 - config['main_wall_width'],
                 -math.pi, math.pi, config['main_wall_width'], config['main_wall_resolution'], wall_img)

# Trial walls
walls = []
for _ in range(0):
    walls.append(WallFactory.create_wall())


# Trial players
players_and_goals = PlayerFactory.create_player(0, 4)
players = players_and_goals[0]
goals = players_and_goals[1]

# Trial ball
trial_ball = Ball(config['screen_width'] / 2, config['screen_height'] / 2,
                  10, -math.pi/2, config['ball_speed'],
                  (255, 255, 255), "")

# Main game loop
run = True
clock = pygame.time.Clock()  # FPS Control

while run:
    # Screen color filler
    screen.fill(tuple(config['background_color']))

    players_and_keys = [[player, movement_key] for player, movement_key in
                        list(zip_longest(players, keys_groups, fillvalue=[]))]

    # Event getter
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close the game
            run = False

        if event.type == pygame.KEYDOWN:
            # Players movement
            for player_and_keys in players_and_keys:
                if not isinstance(player_and_keys[0], BotPlayer):
                    if event.key == player_and_keys[1][0]:
                        player_and_keys[0].rotates_clockwise()
                    if event.key == player_and_keys[1][1]:
                        player_and_keys[0].rotates_counterclockwise()

        if event.type == pygame.KEYUP:
            # Players movement
            for player_and_keys in players_and_keys:
                if not isinstance(player_and_keys[0], BotPlayer):
                    if event.key == player_and_keys[1][0]:
                        player_and_keys[0].not_rotates_clockwise()
                    if event.key == player_and_keys[1][1]:
                        player_and_keys[0].not_rotates_counterclockwise()

    # Main environment drawing
    main_wall.draw(screen)
    for wall in walls:
        wall.draw(screen)

    # Trial player drawing
    index = 0
    for player in players:
        if isinstance(player, BotPlayer):
            player.chase_ball(trial_ball, goals[index])
        player.move(goals[index])
        player.draw(screen)
        # print(player.get_id(), player.get_score())
        # print(player._id, player.starting_angle(), goals[index].starting_angle())
        # print(player.ending_angle(), goals[index].ending_angle())
        index += 1

    for goal in goals:
        goal.draw(screen)

    # Trial ball drawing
    trial_ball.move([main_wall, ] + walls + players + goals)
    trial_ball.draw(screen)

    pygame.display.flip()  # Screen update
    clock.tick(config['fps'])  # FPS control

# Pygame ended
pygame.quit()
