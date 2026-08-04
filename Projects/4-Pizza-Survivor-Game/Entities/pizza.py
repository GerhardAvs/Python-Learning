import pygame

import config
import settings

##
# @file pizza.py
# @brief Gestiona las pizzas lanzadas por el repartidor.
#
# Este módulo contiene las funciones encargadas de crear, mover,
# dibujar y eliminar las pizzas utilizadas como proyectiles
# durante la partida.

##
# @brief Dibuja todas las pizzas activas en la pantalla.
#
# Recorre la lista de pizzas activas y renderiza cada una
# en su posición correspondiente.
#
# @return None
def draw_pizzas():
    for p in config.pizzas:
        config.pantalla.blit(config.pizza_img, (p["x"], p["y"]))


##
# @brief Lanza una pizza hacia la posición indicada por el jugador.
#
# La pizza se genera en el borde del repartidor, en la dirección
# del disparo, y respeta el tiempo de espera entre disparos.
#
# @param click_pos Posición del cursor donde el jugador hizo clic.
# @return bool Devuelve True si la pizza fue lanzada correctamente o
# False si el disparo fue cancelado por el tiempo de recarga o por
# hacer clic exactamente sobre el repartidor.
def launch_pizza(click_pos):

    ahora = pygame.time.get_ticks()

    if ahora - config.last_pizza_throw < settings.TIME_BETWEEN_PIZZAS:
        return False

    config.last_pizza_throw = ahora

    # Centro del repartidor.
    centro_x = config.delivery_pos_x + settings.DELIVERY_SIZE[0] / 2
    centro_y = config.delivery_pos_y + settings.DELIVERY_SIZE[1] / 2

    dx = click_pos[0] - centro_x
    dy = click_pos[1] - centro_y
    distancia = (dx ** 2 + dy ** 2) ** 0.5

    if distancia == 0:
        return False

    # Vector unitario de dirección.
    dir_x = dx / distancia
    dir_y = dy / distancia

    # Punto donde aparece la pizza.
    spawn_x = (
        centro_x
        + dir_x * (settings.DELIVERY_SIZE[0] / 2)
        - settings.PIZZA_SIZE[0] / 2
    )

    spawn_y = (
        centro_y
        + dir_y * (settings.DELIVERY_SIZE[1] / 2)
        - settings.PIZZA_SIZE[1] / 2
    )

    config.pizzas.append({
        "x": spawn_x,
        "y": spawn_y,
        "dx": dir_x * settings.PIZZA_SPEED,
        "dy": dir_y * settings.PIZZA_SPEED,
    })

    return True


##
# @brief Actualiza la posición de todas las pizzas activas.
#
# Cada pizza avanza siguiendo la dirección calculada
# al momento de ser lanzada.
#
# @return None
def move_pizzas():
    for p in config.pizzas:
        p["x"] += p["dx"]
        p["y"] += p["dy"]


##
# @brief Elimina las pizzas que salen de la pantalla.
#
# Esta función evita que la lista de proyectiles siga creciendo
# al descartar las pizzas que ya no son visibles.
#
# @return None
def remove_offscreen_pizzas():
    ancho, alto = settings.WINDOW_SIZE

    config.pizzas = [
        p for p in config.pizzas
        if -settings.PIZZA_SIZE[0] < p["x"] < ancho
        and -settings.PIZZA_SIZE[1] < p["y"] < alto
    ]