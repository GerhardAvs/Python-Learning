import pygame

#initializa pygame
pygame.init()

import config, settings
from System import game
  
game = game.Game()

config.pantalla = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.FULLSCREEN)
config.pantalla.blit(config.background, config.window_origin)
pygame.display.set_caption("Pizza Survivor")
pygame.display.set_icon(config.icon)

game.running()


pygame.quit()