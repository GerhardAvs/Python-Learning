import pygame
import config, settings

def draw_cat(pos_x, pos_y):
    """
    Dibuja el gato en la pantalla en la posición especificada.
    
    Args:
        pos_x (int): La coordenada x para la posición del gato.
        pos_y (int): La coordenada y para la posición del gato.
    """
    config.pantalla.blit(config.cat_img, (pos_x, pos_y))
    

def cat_spawn_outside_screen():
    ...