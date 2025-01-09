import pygame
from entities.Player import Player
from entities.BotPlayer import BotPlayer
from environment.Wall import Wall

# Pygame initialized
pygame.init()

# Main game loop
run = True

while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Close the game
            run = False

# Pygame ended
pygame.quit()
