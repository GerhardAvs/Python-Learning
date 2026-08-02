import pygame
import config, settings
from Entities import dog as dog_entity


def check_mask_collision(pos1, mask1, pos2, mask2):
    """
    Colisión pixel-perfect entre dos sprites usando sus máscaras.
    offset = diferencia de posición entre ambas, requerida por mask.overlap().
    """
    offset = (int(pos2[0] - pos1[0]), int(pos2[1] - pos1[1]))
    return mask1.overlap(mask2, offset) is not None


def resolve_pizza_dog_collisions():
    """
    Revisa todas las pizzas activas contra el perro (si está vivo).
    Si alguna pizza lo toca: elimina esa pizza y mata al perro
    (que reaparece solo, 1s después, gracias a dog.update_dog()).
    """
    if not config.dog_alive:
        return

    dog_pos = (config.dog_pos_x, config.dog_pos_y)
    pizzas_restantes = []

    for p in config.pizzas:
        pizza_pos = (p["x"], p["y"])
        if config.dog_alive and check_mask_collision(pizza_pos, config.pizza_mask, dog_pos, config.dog_mask):
            dog_entity.kill_dog()
        else:
            pizzas_restantes.append(p)

    config.pizzas = pizzas_restantes
    
def resolve_dog_delivery_collision():
    """
    Si el perro toca al repartidor, resta 1 vida (config.delivery_lives).

    Usa DELIVERY_HIT_COOLDOWN para no descontar vidas en cada frame
    mientras el perro se queda pegado al repartidor (sin esto, 9 vidas
    se perderían en menos de un segundo).
    """
    if not config.dog_alive or config.delivery_lives <= 0:
        return

    ahora = pygame.time.get_ticks()
    if ahora - config.delivery_last_hit_time < settings.DELIVERY_HIT_COOLDOWN:
        return

    dog_pos = (config.dog_pos_x, config.dog_pos_y)
    delivery_pos = (config.delivery_pos_x, config.delivery_pos_y)

    if check_mask_collision(dog_pos, config.dog_mask, delivery_pos, config.delivery_mask):
        config.delivery_lives = max(0, config.delivery_lives - 1)
        config.delivery_last_hit_time = ahora
        