import config
import settings


def draw_score():
    """
    Dibuja el puntaje actual en la esquina superior izquierda (0, 0).
    Perro = settings.DOG_SCORE puntos, gato = settings.CAT_SCORE puntos
    (ver System/collisions.py:_kill_enemy, que suma config.score).
    """
    texto = config.score_font.render(f"Score:{config.score}", True, settings.SCORE_TEXT_COLOR)
    config.pantalla.blit(texto, settings.SCORE_POSITION)