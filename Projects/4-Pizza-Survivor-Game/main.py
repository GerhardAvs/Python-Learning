import pygame

##
# @file main.py
# @brief Punto de entrada del juego Pizza Survivor.
#
# Inicializa Pygame, crea la instancia principal del juego,
# ejecuta el bucle principal y libera los recursos al finalizar.

# Inicializa todos los módulos de Pygame.
pygame.init()

from System import Game

##
# @brief Instancia principal del juego.
game = Game()

##
# @brief Ejecuta el bucle principal del juego.
game.run()

##
# @brief Cierra todos los módulos de Pygame y libera los recursos utilizados.
pygame.quit()