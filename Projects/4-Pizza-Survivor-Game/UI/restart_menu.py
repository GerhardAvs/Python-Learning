import pygame

import config
import settings


def draw_restart_menu():
    """Muestra el menú de reinicio cuando el jugador pierde todas las vidas.
    """
    # Aquí iría el código para mostrar el menú de reinicio, con opciones para reiniciar o salir.
    if config.delivery_lives <= 0:
            overlay = pygame.Surface(settings.WINDOW_SIZE, pygame.SRCALPHA)
            overlay.fill((*settings.MENU_OVERLAY_COLOR, settings.MENU_OVERLAY_ALPHA))
            config.pantalla.blit(overlay, (0, 0))

            mouse_pos = pygame.mouse.get_pos()

            for rect, label in zip(config.menu_button_rects, config.menu_button_labels):
                color = (
                    settings.MENU_BUTTON_HOVER_COLOR
                    if rect.collidepoint(mouse_pos)
                    else settings.MENU_BUTTON_COLOR
                )
                pygame.draw.rect(config.pantalla, color, rect, border_radius=14)

                texto = config.menu_font.render(label, True, settings.MENU_BUTTON_TEXT_COLOR)
                texto_rect = texto.get_rect(center=rect.center)
                config.pantalla.blit(texto, texto_rect)