import math

import pygame
import json
from entities.Player import Player
from entities.BotPlayer import BotPlayer
from environment.Wall import Wall
from entities.Ball import Ball

# Loading configurations from a JSON file
with open('data//config.json', 'r') as f:
    config = json.load(f)

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
trial_wall_1 = Wall(config['screen_width'] / 2 + 20,  config['screen_height'] / 2 - 200,
                    50,
                    -math.pi, math.pi, config['main_wall_width'], config['main_wall_resolution'], wall_img)
trial_wall_2 = Wall(config['screen_width'] - 250,  config['screen_height'] - 250,
                    50,
                    -math.pi, math.pi, config['main_wall_width'], config['main_wall_resolution'], wall_img)
trial_wall_3 = Wall(250,  250,
                    50,
                    -math.pi, math.pi, config['main_wall_width'], config['main_wall_resolution'], wall_img)


# Trial player
trial_player_img = pygame.image.load(f"assests//images//entities//players//trial_player_sprite.png")
trial_player = Player(config['screen_width'] / 2,  config['screen_height'] / 2,
                      config['screen_height'] / 2 - 40,
                      (-math.pi - config['player_length']) / 2, (-math.pi + config['player_length']) / 2,
                      config['main_wall_width'], 20, trial_player_img)

# Trial ball
trial_ball = Ball(config['screen_width'] / 2, config['screen_height'] / 2, 10, -math.pi/2, 5,
                  (255, 255, 255), "")

# Main game loop
run = True
clock = pygame.time.Clock()  # FPS Control

while run:
    # Screen color filler
    screen.fill(tuple(config['background_color']))

    # Event getter
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Close the game
            run = False

    # Main environment drawing
    main_wall.draw(screen)
    trial_wall_1.draw(screen)
    trial_wall_2.draw(screen)
    trial_wall_3.draw(screen)

    # Trial player drawing
    trial_player.draw(screen)

    # Trial ball drawing
    trial_ball.move([main_wall, trial_wall_1, trial_wall_2, trial_wall_3, trial_player])
    trial_ball.draw(screen)

    pygame.display.flip()  # Screen update
    clock.tick(config['fps'])  # FPS control

# Pygame ended
pygame.quit()
