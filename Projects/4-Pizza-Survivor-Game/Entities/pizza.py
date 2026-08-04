import pygame

import config
import settings


def draw_pizzas():
    """Dibuja todas las pizzas activas."""
    for p in config.pizzas:
        config.pantalla.blit(config.pizza_img, (p["x"], p["y"]))


def launch_pizza(click_pos):
    """
    Dispara una pizza desde el repartidor hacia el punto donde se hizo click.

    - Respeta el cooldown TIEMPO_ENTRE_PIZZAS (2s) entre disparos.
    - La pizza NO nace en el centro del repartidor: nace en el borde del
      repartidor, del lado hacia donde se disparó.

    Returns:
        bool: True si la pizza se lanzó de verdad, False si no (por el
        cooldown activo o por hacer click justo sobre el repartidor).
        Quien llame a esta función debe usar este valor para decidir si
        reproduce el sonido de disparo o no.
    """
    ahora = pygame.time.get_ticks()
    if ahora - config.last_pizza_throw < settings.TIME_BETWEEN_PIZZAS:
        return False
    config.last_pizza_throw = ahora

    # Centro real del repartidor (pos_x/pos_y son la esquina, por eso sumamos medio ancho/alto)
    centro_x = config.delivery_pos_x + settings.DELIVERY_SIZE[0] / 2
    centro_y = config.delivery_pos_y + settings.DELIVERY_SIZE[1] / 2

    dx = click_pos[0] - centro_x
    dy = click_pos[1] - centro_y
    distancia = (dx**2 + dy**2)**0.5

    if distancia == 0:
        return False

    # Vector unitario de dirección del disparo
    dir_x = dx / distancia
    dir_y = dy / distancia

    # Punto de aparición: borde del repartidor en la dirección del disparo
    spawn_x = centro_x + dir_x * (settings.DELIVERY_SIZE[0] / 2) - settings.PIZZA_SIZE[0] / 2
    spawn_y = centro_y + dir_y * (settings.DELIVERY_SIZE[1] / 2) - settings.PIZZA_SIZE[1] / 2

    config.pizzas.append({
        "x": spawn_x,
        "y": spawn_y,
        "dx": dir_x * settings.PIZZA_SPEED,
        "dy": dir_y * settings.PIZZA_SPEED,
    })
    return True


def move_pizzas():
    """Mueve todas las pizzas activas en línea recta según su dirección."""
    for p in config.pizzas:
        p["x"] += p["dx"]
        p["y"] += p["dy"]

def remove_offscreen_pizzas():
    """Elimina las pizzas que ya salieron de la pantalla, para no acumularlas en memoria."""
    ancho, alto = settings.WINDOW_SIZE
    config.pizzas = [
        p for p in config.pizzas
        if -settings.PIZZA_SIZE[0] < p["x"] < ancho
        and -settings.PIZZA_SIZE[1] < p["y"] < alto
    ]