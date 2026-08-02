import pygame
import settings
from Entities import dog,cat

#///////////////////////////////////  Nombre de la app & Icono de la app ////////////////////////////////////////////////////
window_origin = (0,0)
icon_path = "Resources\\images\\pizza.png"
icon = pygame.image.load(icon_path)

#/////////////////////////////////////////  Cargar Fondo ///////////////////////////////////////////////////////
bakground_path = "Resources\\images\\fondo.png"

background = pygame.image.load(bakground_path)
background = pygame.transform.smoothscale(background, settings.WINDOW_SIZE) #Escala, rotacion 


#///////////////////////////////////  Cargar Personaje (repartidor) ///////////////////////////////////////////////////////
delivery_path = "Resources\\images\\repartidor.png"
#Ajusta la escala (128,200) window_size[0]/15, window_size[1]/5.4

delivery_img = pygame.image.load(delivery_path)
delivery_img = pygame.transform.smoothscale(delivery_img, settings.DELIVERY_SIZE)
delivery_mask = pygame.mask.from_surface(delivery_img)


#///////////////////////////////////    deliver ubication         /////////////////////////////////////////////////
delivery_pos_x = settings.WINDOW_SIZE[0]/2 - settings.DELIVERY_SIZE[0]/2
delivery_pos_y = settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1] - 10

delivery_change_pos_x = 0
delivery_change_pos_y = 0

delivery_lives = settings.DELIVERY_LIVES
delivery_last_hit_time = 0

#////////////////////////////////////////  Lanzamiento de pizzas ///////////////////////////////////////////////////////
pizza_path = "Resources\\images\\pizza.png"
pizza_img = pygame.image.load(pizza_path)
pizza_img = pygame.transform.smoothscale(pizza_img, settings.PIZZA_SIZE)
pizza_mask = pygame.mask.from_surface(pizza_img)


pizzas = []
last_pizza_throw = 0

#//////////////////////////////////////    Cargar Perro ///////////////////////////////////////////////////////
dog_path = "Resources\\images\\perro.png"
#Ajusta la escala (108,128) window_size[0]/17.777, window_size[1]/8.43

dog_img = pygame.image.load(dog_path)
dog_img = pygame.transform.smoothscale(dog_img, settings.DOG_SIZE)
dog_mask = pygame.mask.from_surface(dog_img)

dog_pos_x, dog_pos_y = dog.dog_spawn_outside_screen()

dx_dog = 0
dy_dog = 0
distance_dog = 0

dog_alive = True
dog_death_time = 0
#////////////////////////////////////////    Cargar Gato ///////////////////////////////////////////////////////
cat_path = "Resources\\images\\gato.png"
cat_img = pygame.image.load(cat_path)
cat_img = pygame.transform.smoothscale(cat_img, settings.CAT_SIZE)

#cat_pos_x, cat_pos_y = cat.cat_spawn_outside_screen()

dx_cat = 0
dy_cat = 0
distance_cat = 0
#////////////////////////////////////////    Cargar Corazones (vidas)  ///////////////////////////////////////
corazon_path = "Resources\\images\\corazon.png"

corazon_img_full = pygame.transform.smoothscale(pygame.image.load(corazon_path), settings.HEART_SIZE_FULL)
corazon_img_medium = pygame.transform.smoothscale(pygame.image.load(corazon_path), settings.HEART_SIZE_MEDIUM)
corazon_img_small = pygame.transform.smoothscale(pygame.image.load(corazon_path), settings.HEART_SIZE_SMALL)

# fila de 3 corazones en la esquina superior derecha (antes ahí estaba el botón de salir)
_hearts_total_width = 3 * settings.HEART_SLOT_SIZE[0] + 2 * settings.HEART_SPACING
hearts_start_x = settings.WINDOW_SIZE[0] - settings.HEART_MARGIN_RIGHT - _hearts_total_width
hearts_y = settings.HEART_MARGIN_TOP

hearts_slot_positions = [
    (hearts_start_x + i * (settings.HEART_SLOT_SIZE[0] + settings.HEART_SPACING), hearts_y)
    for i in range(3)
]

#////////////////////////////////////////    Menú de pausa  ///////////////////////////////////////////////////
game_paused = False

menu_font = pygame.font.SysFont(None, 40)
menu_button_labels = ["Reanudar", "Cambiar de traje", "Salir"]
menu_button_actions = ["reanudar", "traje", "salir"]

_menu_button_w, _menu_button_h = settings.MENU_BUTTON_SIZE
_menu_total_h = 3 * _menu_button_h + 2 * settings.MENU_BUTTON_SPACING
_menu_start_y = settings.WINDOW_SIZE[1] / 2 - _menu_total_h / 2
_menu_x = settings.WINDOW_SIZE[0] / 2 - _menu_button_w / 2

menu_button_rects = [
    pygame.Rect(
        _menu_x,
        _menu_start_y + i * (_menu_button_h + settings.MENU_BUTTON_SPACING),
        _menu_button_w,
        _menu_button_h,
    )
    for i in range(3)
]


