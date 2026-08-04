import pygame

import config
import settings


def _select_heart_image(lives_in_heart):
    """
    Devuelve la imagen que corresponde según cuántas vidas le quedan
    a ESE corazón puntual (0 a 3). None = el corazón ya se gastó.
    """

    
    if lives_in_heart >= 3:
        return config.corazon_img_full
    if lives_in_heart == 2:
        return config.corazon_img_medium
    if lives_in_heart == 1:
        return config.corazon_img_small
    
    return None


def draw_hearts():
    """
    Dibuja los 3 corazones en fila, en la esquina superior derecha.

    Cada corazón vale 3 vidas de config.delivery_lives (9 en total).
    Se consumen de izquierda a derecha: primero se achica y borra el
    corazón 0 (el de más a la izquierda), luego el corazón 1, y por
    último el corazón 2 (el de más a la derecha).

    Por corazón:
        3 vidas restantes -> tamaño normal
        2 vidas restantes -> se achica
        1 vida  restante  -> se achica más
        0 vidas restantes -> desaparece
    """
    golpes_recibidos = settings.DELIVERY_LIVES - config.delivery_lives
    for i, (slot_x, slot_y) in enumerate(config.hearts_slot_positions):
        golpes_de_este_corazon = max(0, min(3, golpes_recibidos - i * 3))
        lives_in_heart = 3 - golpes_de_este_corazon

        heart_img = _select_heart_image(lives_in_heart)
        if heart_img is None:
            continue  # este corazón ya se gastó, no se dibuja

        slot_w, slot_h = settings.HEART_SLOT_SIZE
        img_w, img_h = heart_img.get_size()
        pos_x = slot_x + (slot_w - img_w) / 2
        pos_y = slot_y + (slot_h - img_h) / 2

        config.pantalla.blit(heart_img, (pos_x, pos_y))
