import pygame

import config
import settings
from Entities.enemy import Enemy


class Cat(Enemy):
    def __init__(self):
        super().__init__(
            config.cat_path,
            settings.CAT_SPEED,
            settings.CAT_SIZE,
            settings.CAT_RESPAWN_DELAY,
            settings.CAT_SCORE,
        )