import pygame
import config, settings

def draw_exit_button(pos_x, pos_y):
    """
    Draw the exit button on the screen at the specified position.
    
    Args:
        pos_x (int): The x-coordinate for the exit button's position.
        pos_y (int): The y-coordinate for the exit button's position.
    """
    config.pantalla.blit(config.btnSalir_img, (pos_x, pos_y))
    
def exit_button(mouse_pos):
    """
    Verifica si se presionó el botón de salir.

    Args:
        mouse_pos (tuple): Posición (x, y) del mouse.

    Returns:
        bool: False si se presionó el botón de salir, True en caso contrario.
    """

def exit_button(mouse_pos):
    return config.btnSalir_rect.collidepoint(mouse_pos)