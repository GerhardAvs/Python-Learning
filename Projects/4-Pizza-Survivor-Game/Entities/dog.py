import pygame

import config
import settings
from Entities.enemy import Enemy


class Dog(Enemy):
    def __init__(self):
        super().__init__(
            config.dog_path,
            settings.DOG_SPEED,
            settings.DOG_SIZE,
            settings.DOG_RESPAWN_DELAY,
            settings.DOG_SCORE,
        )