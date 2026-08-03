import pygame

import config
import settings


def check_mask_collision(pos1, mask1, pos2, mask2):
    """
    Colisión pixel-perfect entre dos sprites usando sus máscaras.
    offset = diferencia de posición entre ambas, requerida por mask.overlap().
    """
    offset = (int(pos2[0] - pos1[0]), int(pos2[1] - pos1[1]))
    return mask1.overlap(mask2, offset) is not None


def resolve_pizza_enemy_collisions(enemy):
    """
    Revisa todas las pizzas activas contra un enemigo (si está vivo).
    Si alguna pizza lo toca: elimina esa pizza y mata al enemigo
    (que reaparece solo, gracias a enemy.update()).

    Args:
        enemy (Enemy): instancia del enemigo a revisar (dog, cat, etc.).
    """
    if not enemy.alive:
        return

    pizzas_restantes = []

    for pizza in config.pizzas:
        pizza_pos = (pizza["x"], pizza["y"])
        if enemy.alive and check_mask_collision(pizza_pos, config.pizza_mask, enemy.pos, enemy.mask):
            enemy.kill()
        else:
            pizzas_restantes.append(pizza)

    config.pizzas = pizzas_restantes


def resolve_enemy_delivery_collision(enemy):
    """
    Si el enemigo toca al repartidor, resta 1 vida (config.delivery_lives).

    Usa DELIVERY_HIT_COOLDOWN para no descontar vidas en cada frame
    mientras el enemigo se queda pegado al repartidor (sin esto, 9 vidas
    se perderían en menos de un segundo).

    Args:
        enemy (Enemy): instancia del enemigo a revisar (dog, cat, etc.).
    """
    if not enemy.alive or config.delivery_lives <= 0:
        return

    ahora = pygame.time.get_ticks()
    if ahora - config.delivery_last_hit_time < settings.DELIVERY_HIT_COOLDOWN:
        return

    delivery_pos = (config.delivery_pos_x, config.delivery_pos_y)

    if check_mask_collision(enemy.pos, enemy.mask, delivery_pos, config.delivery_mask):
        config.delivery_lives = max(0, config.delivery_lives - 1)
        config.delivery_last_hit_time = ahora