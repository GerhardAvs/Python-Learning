import pygame

info = pygame.display.Info()

#///////////////////////////////////////// Pantalla ///////////////////////////////////////////////////////////
WINDOW_WIDTH = info.current_w
WINDOW_HEIGHT = info.current_h
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

#/////////////////////////////////////////  Juego /////////////////////////////////////////////////////////////
FPS = 200
VOLUME = 0.5
TITLE = "Pizza Survivor"

#/////////////////////////////////////////  Velocidades ///////////////////////////////////////////////////////
DELIVERY_SPEED = 6
DOG_SPEED = 4
PIZZA_SPEED = 8
CAT_SPEED = 5
#/////////////////////////////////////////  Escalas ///////////////////////////////////////////////////////////
DELIVERY_SIZE = (128, 200)
DOG_SIZE = (108, 128)
CAT_SIZE = (108, 128)
BTN_EXIT_SIZE = (250, 250)
PIZZA_SIZE = (60, 60)

#/////////////////////////////////////////// cooldowns ///////////////////////////////////////////////////////
TIME_BETWEEN_PIZZAS = 1000
DOG_RESPAWN_DELAY = CAT_RESPAWN_DELAY = 3000
DELIVERY_HIT_COOLDOWN = 1000

#/////////////////////////////////////////// vidas / corazones ///////////////////////////////////////////////
DELIVERY_LIVES = 9  # 3 corazones x 3 vidas cada uno

HEART_SLOT_SIZE = (80, 80)     # espacio reservado para cada corazón (para que no "salten" al achicarse)
HEART_SIZE_FULL = (80, 80)     # 3 vidas en ese corazón
HEART_SIZE_MEDIUM = (64, 64)   # 2 vidas en ese corazón
HEART_SIZE_SMALL = (40, 40)    # 1 vida en ese corazón
HEART_SPACING = 12             # separación entre corazones
HEART_MARGIN_RIGHT = 30        # separación entre los corazones y el borde derecho
HEART_MARGIN_TOP = 30          # separación entre los corazones y el borde superior
#HEART_TOTAL_LIVES = 9          # 3 corazones x 3 vidas cada uno
#/////////////////////////////////////////// menú de pausa ////////////////////////////////////////////////////
MENU_BUTTON_SIZE = (340, 80)
MENU_BUTTON_SPACING = 30
MENU_BUTTON_COLOR = (0,0,0)
MENU_BUTTON_HOVER_COLOR = (255, 130, 70)
MENU_BUTTON_TEXT_COLOR = (255, 255, 255)
MENU_OVERLAY_COLOR = (0, 0, 0)
MENU_OVERLAY_ALPHA = 180        # 0-255, qué tan oscuro se pone el fondo al pausar
MENU_ICON_SIZE = (48, 48)

#/////////////////////////////////////////// puntaje ///////////////////////////////////////////////////////
DOG_SCORE = 10
CAT_SCORE = 15
SCORE_FONT_SIZE = 40
SCORE_TEXT_COLOR = (255, 255, 255)
SCORE_POSITION = (20, 20)   # esquina superior izquierda

#/////////////////////////////////////////// enemigos extra ////////////////////////////////////////////////
# Antes solo aparecía un perro nuevo cuando el anterior moría (y lo mismo con
# el gato). Ahora, cada EXTRA_ENEMY_SPAWN_INTERVAL ms se agrega un enemigo
# nuevo sin importar si los anteriores siguen vivos, hasta llegar a MAX_ENEMIES.
MAX_ENEMIES = 6
EXTRA_ENEMY_SPAWN_INTERVAL = 6000