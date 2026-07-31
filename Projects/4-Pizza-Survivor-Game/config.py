import pygame
import settings
from random import randint

#///////////////////////////////////  Nombre de la app & Icono de la app ////////////////////////////////////////////////////
window_origin = (0,0)
icon_path = "Resources\\images\\pizza.png"
icon = pygame.image.load(icon_path)

#///////////////////////////////////////  boton de salida ///////////////////////////////////////////////////////
btnSalir_path = "Resources\\images\\BtnSalir.png"

btnSalir_img = pygame.image.load(btnSalir_path)
btnSalir_img = pygame.transform.scale(btnSalir_img, settings.BTN_EXIT_SIZE)

btnSalir_rect = btnSalir_img.get_rect()

btnSalir_pos_x = settings.WINDOW_SIZE[0] - settings.BTN_EXIT_SIZE[0]
btnSalir_pos_y = -settings.BTN_EXIT_SIZE[1] / 3

btnSalir_rect.topright = (
    btnSalir_pos_x,
    btnSalir_pos_y  
)

#/////////////////////////////////////////  Cargar Fondo ///////////////////////////////////////////////////////
bakground_path = "Resources\\images\\fondo.png"

background = pygame.image.load(bakground_path)
background = pygame.transform.scale(background, settings.WINDOW_SIZE) #Escala, rotacion 


#///////////////////////////////////  Cargar Personaje (repartidor) ///////////////////////////////////////////////////////
delivery_path = "Resources\\images\\repartidor.png"
#Ajusta la escala (128,200) window_size[0]/15, window_size[1]/5.4

delivery_img = pygame.image.load(delivery_path)
delivery_img = pygame.transform.scale(delivery_img, settings.DELIVERY_SIZE)


#///////////////////////////////////    deliver ubication         /////////////////////////////////////////////////
delivery_pos_x = settings.WINDOW_SIZE[0]/2 - settings.DELIVERY_SIZE[0]/2
delivery_pos_y = settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1] - 10

delivery_change_pos_x = 0
delivery_change_pos_y = 0


#//////////////////////////////////////    Cargar Perro ///////////////////////////////////////////////////////
dog_path = "Resources\\images\\perro.png"
#Ajusta la escala (108,128) window_size[0]/17.777, window_size[1]/8.43

dog_img = pygame.image.load(dog_path)
dog_img = pygame.transform.scale(dog_img, settings.DOG_SIZE)

dog_pos_x = randint(0,746)
dog_pos_y = 0


