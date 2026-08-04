import pygame

import config
import settings

##
# @file delivery.py
# @brief Gestiona el movimiento y dibujo del repartidor.
#
# Este módulo contiene las funciones encargadas de dibujar al
# repartidor, actualizar su movimiento, procesar las entradas
# del teclado y mantener al personaje dentro de los límites
# de la pantalla.

##
# @brief Dibuja al repartidor en la pantalla.
#
# @param pos_x Posición horizontal donde se dibujará el repartidor.
# @param pos_y Posición vertical donde se dibujará el repartidor.
# @return None
def draw_delivery(pos_x, pos_y):
    config.pantalla.blit(config.delivery_img, (pos_x, pos_y))


##
# @brief Actualiza la posición del repartidor.
#
# Modifica la posición del personaje utilizando la velocidad
# almacenada en las variables de movimiento.
#
# @return None
def move_delivery():
    config.delivery_pos_x += config.delivery_change_pos_x
    config.delivery_pos_y += config.delivery_change_pos_y


##
# @brief Actualiza el movimiento según la tecla presionada.
#
# @param event Código de la tecla presionada.
# @return None
def get_delivery_movement(event):

    if event == pygame.K_a:
        config.delivery_change_pos_x = -settings.DELIVERY_SPEED

    if event == pygame.K_d:
        config.delivery_change_pos_x = settings.DELIVERY_SPEED

    if event == pygame.K_w:
        config.delivery_change_pos_y = -settings.DELIVERY_SPEED

    if event == pygame.K_s:
        config.delivery_change_pos_y = settings.DELIVERY_SPEED


##
# @brief Detiene el movimiento cuando se libera una tecla.
#
# @param event Código de la tecla liberada.
# @return None
def reset_delivery_movement(event):

    if event in (pygame.K_a, pygame.K_d):
        config.delivery_change_pos_x = 0

    if event in (pygame.K_w, pygame.K_s):
        config.delivery_change_pos_y = 0


##
# @brief Limita el movimiento del repartidor a la ventana del juego.
#
# Evita que el personaje salga de los límites visibles de la pantalla.
#
# @return None
def delivery_restrictions():

    if config.delivery_pos_x < 0:
        config.delivery_pos_x = 0

    elif config.delivery_pos_x > settings.WINDOW_SIZE[0] - settings.DELIVERY_SIZE[0]:
        config.delivery_pos_x = settings.WINDOW_SIZE[0] - settings.DELIVERY_SIZE[0]

    if config.delivery_pos_y < 0:
        config.delivery_pos_y = 0

    elif config.delivery_pos_y > settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1]:
        config.delivery_pos_y = settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1]