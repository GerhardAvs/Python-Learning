import pygame
import pygame

info = pygame.display.Info()

#///////////////////////////////////////// Pantalla ///////////////////////////////////////////////////////
WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

#/////////////////////////////////////////  Juego ///////////////////////////////////////////////////////
FPS = 60
TITLE = "Pizza Survivor"

#/////////////////////////////////////////  Velocidades ///////////////////////////////////////////////////////
DELIVERY_SPEED = 4
DOG_SPEED = 2
PIZZA_SPEED = 6
CAT_SPEED = 3
#/////////////////////////////////////////  Escalas ///////////////////////////////////////////////////////
DELIVERY_SIZE = (128, 200)
DOG_SIZE = (108, 128)
BTN_EXIT_SIZE = (250, 250)
PIZZA_SIZE = (60, 60)

#/////////////////////////////////////////// cooldowns ///////////////////////////////////////////////////////
TIME_BETWEEN_PIZZAS = 1000
DOG_RESPAWN_DELAY = 3000
DELIVERY_HIT_COOLDOWN = 1000

#/////////////////////////////////////////// vidas / corazones ///////////////////////////////////////////////
DELIVERY_LIVES = 9  # 3 corazones x 3 vidas cada uno

HEART_SLOT_SIZE = (60, 60)     # espacio reservado para cada corazón (para que no "salten" al achicarse)
HEART_SIZE_FULL = (60, 60)     # 3 vidas en ese corazón
HEART_SIZE_MEDIUM = (44, 44)   # 2 vidas en ese corazón
HEART_SIZE_SMALL = (30, 30)    # 1 vida en ese corazón
HEART_SPACING = 12             # separación entre corazones
HEART_MARGIN_RIGHT = 30        # separación entre los corazones y el borde derecho
HEART_MARGIN_TOP = 30           # separación entre los corazones y el borde superior

#/////////////////////////////////////////// menú de pausa ////////////////////////////////////////////////////
MENU_BUTTON_SIZE = (340, 80)
MENU_BUTTON_SPACING = 30
MENU_BUTTON_COLOR = (0,0,0)
MENU_BUTTON_HOVER_COLOR = (255, 130, 70)
MENU_BUTTON_TEXT_COLOR = (255, 255, 255)
MENU_OVERLAY_COLOR = (0, 0, 0)
MENU_OVERLAY_ALPHA = 180        # 0-255, qué tan oscuro se pone el fondo al pausar
MENU_ICON_SIZE = (48, 48)