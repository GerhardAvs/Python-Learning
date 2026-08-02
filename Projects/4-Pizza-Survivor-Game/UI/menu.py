import pygame
import config, settings


def draw_pause_menu():
    """
    Dibuja el menú de pausa: un overlay semitransparente sobre todo el
    juego (que se ve "congelado" atrás) y 3 botones en columna,
    centrados en la pantalla: Reanudar, Cambiar de traje, Salir.
    """
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

    # ícono del botón de salir original, como acento visual dentro del botón "Salir"
    salir_rect = config.menu_button_rects[2]
    icono_rect = config.menu_salir_icon_img.get_rect(
        midright=(salir_rect.right - 16, salir_rect.centery)
    )
    config.pantalla.blit(config.menu_salir_icon_img, icono_rect)


def handle_menu_click(mouse_pos):
    """
    Revisa si el click cayó en alguno de los 3 botones del menú de pausa.
    Devuelve "reanudar", "traje", "salir", o None si no cayó en ninguno.
    """
    for rect, accion in zip(config.menu_button_rects, config.menu_button_actions):
        if rect.collidepoint(mouse_pos):
            return accion
    return None