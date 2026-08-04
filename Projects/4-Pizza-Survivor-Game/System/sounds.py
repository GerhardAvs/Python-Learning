import pygame

import config
import settings


class SoundManager:
    """Carga y reproduce todos los efectos de sonido y la música de fondo."""

    def __init__(self):
        """Inicializa el mixer de pygame y carga todos los sonidos del juego."""
        pygame.mixer.init()
        self.sounds = self._load_sounds()

    def _load_sounds(self):
        """
        Carga cada sonido desde su ruta (definida en config) y le aplica
        el volumen global de settings.VOLUME.

        Returns:
            dict[str, pygame.mixer.Sound]: sonidos indexados por nombre.
        """
        rutas = {
            "pizza_throw": config.pizza_throw_path,             # al lanzar una pizza
            "enemy_hit": config.enemy_hit_path,                 # al golpear al perro/gato
            "background_music": config.background_music_path,  # música de fondo (loop)
            "lost_life": config.lost_life_path,                 # al perder una vida
        }

        sonidos = {}
        for nombre, ruta in rutas.items():
            sonido = pygame.mixer.Sound(ruta)
            sonido.set_volume(settings.VOLUME)
            sonidos[nombre] = sonido
        return sonidos

    def play_sound(self, sound_name):
        """
        Reproduce un efecto de sonido una sola vez.

        Args:
            sound_name (str): nombre del sonido ("pizza_throw", "enemy_hit", "lost_life", ...).
        """
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def play_background_music(self):
        """Pone la música de fondo en loop infinito (no hace nada si ya está sonando)."""
        self.sounds["background_music"].play(loops=-1)

    def stop_background_music(self):
        """Detiene la música de fondo."""
        self.sounds["background_music"].stop()