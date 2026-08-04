import pygame

import settings

##
# @file config.py
# @brief Configuración global y recursos del juego Pizza Survivor.
#
# Este archivo centraliza la carga de imágenes, sonidos, fuentes,
# posiciones iniciales y variables de estado utilizadas por el juego.
# También define los recursos compartidos entre los distintos módulos.

#///////////////////////////////////  Nombre de la app & Icono de la app ////////////////////////////////////////////////////

##
# @brief Posición inicial de la ventana.
window_origin = (0, 0)

##
# @brief Ruta del icono de la aplicación.
icon_path = "Resources\\images\\pizza.png"

##
# @brief Icono de la ventana del juego.
icon = pygame.image.load(icon_path)

#/////////////////////////////////////////  Cargar Fondo ///////////////////////////////////////////////////////

##
# @brief Ruta de la imagen de fondo.
bakground_path = "Resources\\images\\fondo.png"

##
# @brief Imagen de fondo escalada al tamaño de la ventana.
background = pygame.image.load(bakground_path)
background = pygame.transform.smoothscale(background, settings.WINDOW_SIZE)

#///////////////////////////////////  Cargar Personaje (repartidor) ///////////////////////////////////////////////////////

##
# @brief Ruta de la apariencia actual del repartidor.
delivery_path = "Resources\\images\\Delivery_Skins\\didi_delivery.png"

##
# @brief Imagen del repartidor escalada.
delivery_img = pygame.image.load(delivery_path)
delivery_img = pygame.transform.smoothscale(delivery_img, settings.DELIVERY_SIZE)

##
# @brief Máscara utilizada para detectar colisiones del repartidor.
delivery_mask = pygame.mask.from_surface(delivery_img)

#///////////////////////////////////    Ubicación del repartidor /////////////////////////////////////////////////

##
# @brief Posición horizontal inicial del repartidor.
delivery_pos_x = settings.WINDOW_SIZE[0] / 2 - settings.DELIVERY_SIZE[0] / 2

##
# @brief Posición vertical inicial del repartidor.
delivery_pos_y = settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1] - 10

##
# @brief Velocidad horizontal del repartidor.
delivery_change_pos_x = 0

##
# @brief Velocidad vertical del repartidor.
delivery_change_pos_y = 0

##
# @brief Número de vidas del repartidor.
delivery_lives = settings.DELIVERY_LIVES

##
# @brief Instante del último daño recibido.
delivery_last_hit_time = 0

#////////////////////////////////////////  Lanzamiento de pizzas ///////////////////////////////////////////////////////

##
# @brief Ruta de la imagen de la pizza.
pizza_path = "Resources\\images\\pizza.png"

##
# @brief Imagen escalada de la pizza.
pizza_img = pygame.image.load(pizza_path)
pizza_img = pygame.transform.smoothscale(pizza_img, settings.PIZZA_SIZE)

##
# @brief Máscara de colisión de la pizza.
pizza_mask = pygame.mask.from_surface(pizza_img)

##
# @brief Lista que almacena todas las pizzas activas.
pizzas = []

##
# @brief Tiempo del último lanzamiento de pizza.
last_pizza_throw = 0

#//////////////////////////////////////    Cargar Perro ///////////////////////////////////////////////////////

##
# @brief Ruta de la imagen del perro.
dog_path = "Resources\\images\\perro.png"

##
# @note La imagen, máscara y estado del perro pertenecen a la clase Enemy.

#////////////////////////////////////////    Cargar Gato ///////////////////////////////////////////////////////

##
# @brief Ruta de la imagen del gato.
cat_path = "Resources\\images\\gato.png"

##
# @note La imagen, máscara y estado del gato pertenecen a la clase Enemy.

#////////////////////////////////////////    Cargar Corazones (vidas)  ///////////////////////////////////////

##
# @brief Ruta de la imagen del corazón.
corazon_path = "Resources\\images\\corazon.png"

##
# @brief Corazón de tamaño grande.
corazon_img_full = pygame.transform.smoothscale(
    pygame.image.load(corazon_path),
    settings.HEART_SIZE_FULL
)

##
# @brief Corazón de tamaño mediano.
corazon_img_medium = pygame.transform.smoothscale(
    pygame.image.load(corazon_path),
    settings.HEART_SIZE_MEDIUM
)

##
# @brief Corazón de tamaño pequeño.
corazon_img_small = pygame.transform.smoothscale(
    pygame.image.load(corazon_path),
    settings.HEART_SIZE_SMALL
)

##
# @brief Ancho total ocupado por los tres corazones.
_hearts_total_width = (
    3 * settings.HEART_SLOT_SIZE[0]
    + 2 * settings.HEART_SPACING
)

##
# @brief Coordenada X inicial del primer corazón.
hearts_start_x = (
    settings.WINDOW_SIZE[0]
    - settings.HEART_MARGIN_RIGHT
    - _hearts_total_width
)

##
# @brief Coordenada Y donde se dibujan los corazones.
hearts_y = settings.HEART_MARGIN_TOP

##
# @brief Posiciones donde se dibujará cada corazón.
hearts_slot_positions = [
    (
        hearts_start_x + i * (
            settings.HEART_SLOT_SIZE[0]
            + settings.HEART_SPACING
        ),
        hearts_y,
    )
    for i in range(3)
]

#////////////////////////////////////////    Menú de pausa  ///////////////////////////////////////////////////

##
# @brief Indica si el juego se encuentra pausado.
game_paused = False

##
# @brief Fuente utilizada por el menú de pausa.
menu_font = pygame.font.SysFont(None, 40)

##
# @brief Texto mostrado en cada botón del menú de pausa.
menu_button_labels = [
    "Reanudar",
    "Cambiar de traje",
    "Salir"
]

##
# @brief Acción asociada a cada botón del menú.
menu_button_actions = [
    "reanudar",
    "traje",
    "salir"
]

_menu_button_w, _menu_button_h = settings.MENU_BUTTON_SIZE

##
# @brief Altura total ocupada por el menú.
_menu_total_h = (
    3 * _menu_button_h
    + 2 * settings.MENU_BUTTON_SPACING
)

##
# @brief Posición vertical inicial del menú.
_menu_start_y = (
    settings.WINDOW_SIZE[1] / 2
    - _menu_total_h / 2
)

##
# @brief Posición horizontal del menú.
_menu_x = (
    settings.WINDOW_SIZE[0] / 2
    - _menu_button_w / 2
)

##
# @brief Rectángulos de los botones del menú de pausa.
menu_button_rects = [
    pygame.Rect(
        _menu_x,
        _menu_start_y + i * (
            _menu_button_h
            + settings.MENU_BUTTON_SPACING
        ),
        _menu_button_w,
        _menu_button_h,
    )
    for i in range(3)
]

#///////////////////////////////////////// Restart menu  ///////////////////////////////////////////////////

##
# @brief Etiquetas del menú de reinicio.
restart_menu_button_labels = [
    "Reiniciar",
    "Cambiar de traje",
    "Salir"
]

##
# @brief Acciones del menú de reinicio.
restart_menu_button_actions = [
    "reiniciar",
    "traje",
    "salir"
]

#/////////////////////////////////////////// Sounds /////////////////////////////////////////////////////

##
# @brief Ruta del sonido al lanzar una pizza.
pizza_throw_path = "Resources\\sounds\\disparo.mp3"

##
# @brief Ruta del sonido cuando un enemigo recibe un impacto.
enemy_hit_path = "Resources\\sounds\\golpe.mp3"

##
# @brief Ruta de la música de fondo.
background_music_path = "Resources\\sounds\\MusicaFondo.mp3"

##
# @brief Ruta del sonido al perder una vida.
lost_life_path = "Resources\\sounds\\vida_perdida.mp3"

#/////////////////////////////////////////// Puntaje ////////////////////////////////////////////////////

##
# @brief Puntaje actual del jugador.
score = 0

##
# @brief Fuente utilizada para mostrar el puntaje.
score_font = pygame.font.SysFont(
    None,
    settings.SCORE_FONT_SIZE
)

#/////////////////////////////////////////// Estado de la partida //////////////////////////////////////

##
# @brief Indica si la partida ha terminado.
game_over = False