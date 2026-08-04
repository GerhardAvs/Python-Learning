import pygame

import config
import settings


def draw_restart_menu():
    """
    Dibuja el menú de reinicio: overlay semitransparente + 3 botones
    (Reiniciar, Cambiar de traje, Salir). Se muestra cuando el repartidor
    se queda sin vidas (config.game_over == True). Usa el mismo layout de
    botones que el menú de pausa (config.menu_button_rects).
    """
    overlay = pygame.Surface(settings.WINDOW_SIZE, pygame.SRCALPHA)
    overlay.fill((*settings.MENU_OVERLAY_COLOR, settings.MENU_OVERLAY_ALPHA))
    config.pantalla.blit(overlay, (0, 0))

    mouse_pos = pygame.mouse.get_pos()

    for rect, label in zip(config.menu_button_rects, config.restart_menu_button_labels):
        color = (
            settings.MENU_BUTTON_HOVER_COLOR
            if rect.collidepoint(mouse_pos)
            else settings.MENU_BUTTON_COLOR
        )
        pygame.draw.rect(config.pantalla, color, rect, border_radius=14)

        texto = config.menu_font.render(label, True, settings.MENU_BUTTON_TEXT_COLOR)
        texto_rect = texto.get_rect(center=rect.center)
        config.pantalla.blit(texto, texto_rect)


def handle_restart_menu_click(mouse_pos):
    """
    Revisa si el click cayó en alguno de los 3 botones del menú de reinicio.
    Devuelve "reiniciar", "traje", "salir", o None si no cayó en ninguno.
    """
    for rect, accion in zip(config.menu_button_rects, config.restart_menu_button_actions):
        if rect.collidepoint(mouse_pos):
            return accion
    return None