import pygame

##
# @file settings.py
# @brief Configuración global del juego Pizza Survivor.
#
# Este archivo contiene todas las constantes utilizadas por el juego,
# incluyendo configuración de la ventana, velocidades, tamaños,
# tiempos de espera, colores, puntajes y límites de enemigos.

##
# @brief Obtiene la información de la pantalla principal del sistema.
info = pygame.display.Info()

#///////////////////////////////////////// Pantalla ///////////////////////////////////////////////////////////

##
# @brief Ancho de la pantalla del usuario en píxeles.
WINDOW_WIDTH = info.current_w

##
# @brief Alto de la pantalla del usuario en píxeles.
WINDOW_HEIGHT = info.current_h

##
# @brief Tamaño de la ventana del juego.
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

#///////////////////////////////////////// Juego /////////////////////////////////////////////////////////////

##
# @brief Límite máximo de fotogramas por segundo.
FPS = 200

##
# @brief Volumen general del juego.
VOLUME = 0.5

##
# @brief Título de la ventana.
TITLE = "Pizza Survivor"

#///////////////////////////////////////// Velocidades ///////////////////////////////////////////////////////

##
# @name Velocidades de las entidades
# @{
DELIVERY_SPEED = 6
DOG_SPEED = 4
PIZZA_SPEED = 8
CAT_SPEED = 5
## @}

#///////////////////////////////////////// Escalas ///////////////////////////////////////////////////////////

##
# @name Tamaños de los sprites
# @{
DELIVERY_SIZE = (128, 200)
DOG_SIZE = (108, 128)
CAT_SIZE = (108, 128)
BTN_EXIT_SIZE = (250, 250)
PIZZA_SIZE = (60, 60)
## @}

#/////////////////////////////////////////// Cooldowns ///////////////////////////////////////////////////////

##
# @brief Tiempo mínimo entre lanzamientos de pizza (ms).
TIME_BETWEEN_PIZZAS = 1000

##
# @brief Tiempo de reaparición del perro (ms).
DOG_RESPAWN_DELAY = 3000

##
# @brief Tiempo de reaparición del gato (ms).
CAT_RESPAWN_DELAY = 3000

##
# @brief Tiempo de invulnerabilidad tras recibir daño (ms).
DELIVERY_HIT_COOLDOWN = 1000

#/////////////////////////////////////////// Vidas / Corazones ///////////////////////////////////////////////

##
# @brief Número total de vidas del repartidor.
#
# Cada corazón representa tres vidas.
DELIVERY_LIVES = 9

##
# @brief Espacio reservado para cada corazón.
HEART_SLOT_SIZE = (80, 80)

##
# @brief Tamaño del corazón con tres vidas.
HEART_SIZE_FULL = (80, 80)

##
# @brief Tamaño del corazón con dos vidas.
HEART_SIZE_MEDIUM = (64, 64)

##
# @brief Tamaño del corazón con una vida.
HEART_SIZE_SMALL = (40, 40)

##
# @brief Separación horizontal entre corazones.
HEART_SPACING = 12

##
# @brief Margen derecho de los corazones.
HEART_MARGIN_RIGHT = 30

##
# @brief Margen superior de los corazones.
HEART_MARGIN_TOP = 30

#/////////////////////////////////////////// Menú de pausa ////////////////////////////////////////////////////

##
# @brief Tamaño de los botones del menú.
MENU_BUTTON_SIZE = (340, 80)

##
# @brief Separación entre botones.
MENU_BUTTON_SPACING = 30

##
# @brief Color normal de los botones.
MENU_BUTTON_COLOR = (0, 0, 0)

##
# @brief Color del botón al pasar el cursor.
MENU_BUTTON_HOVER_COLOR = (255, 130, 70)

##
# @brief Color del texto de los botones.
MENU_BUTTON_TEXT_COLOR = (255, 255, 255)

##
# @brief Color del fondo del menú de pausa.
MENU_OVERLAY_COLOR = (0, 0, 0)

##
# @brief Transparencia del fondo del menú.
#
# Valores permitidos entre 0 y 255.
MENU_OVERLAY_ALPHA = 180

##
# @brief Tamaño de los iconos del menú.
MENU_ICON_SIZE = (48, 48)

#/////////////////////////////////////////// Puntaje ///////////////////////////////////////////////////////

##
# @brief Puntos otorgados por eliminar un perro.
DOG_SCORE = 10

##
# @brief Puntos otorgados por eliminar un gato.
CAT_SCORE = 15

##
# @brief Tamaño de la fuente del puntaje.
SCORE_FONT_SIZE = 40

##
# @brief Color del texto del puntaje.
SCORE_TEXT_COLOR = (255, 255, 255)

##
# @brief Posición donde se muestra el puntaje.
SCORE_POSITION = (20, 20)

#/////////////////////////////////////////// Enemigos extra ////////////////////////////////////////////////

##
# @brief Número máximo de enemigos simultáneos.
MAX_ENEMIES = 6

##
# @brief Intervalo entre la aparición de enemigos adicionales.
#
# Expresado en milisegundos.
EXTRA_ENEMY_SPAWN_INTERVAL = 6000