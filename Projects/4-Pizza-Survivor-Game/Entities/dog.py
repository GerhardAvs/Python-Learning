import pygame

import config
import settings
from Entities.enemy import Enemy

##
# @file dog.py
# @brief Define la clase Dog.
#
# Este módulo implementa la clase Dog, que representa un enemigo
# de tipo perro. Hereda el comportamiento general de la clase Enemy
# y configura los atributos específicos de este enemigo.

class Dog(Enemy):
    ##
    # @brief Crea una nueva instancia de un perro.
    #
    # Inicializa el enemigo con la configuración correspondiente
    # al perro, incluyendo su sprite, velocidad, tamaño,
    # tiempo de reaparición y puntaje otorgado al ser eliminado.
    #
    # @return None
    def __init__(self):
        super().__init__(
            config.dog_path,
            settings.DOG_SPEED,
            settings.DOG_SIZE,
            settings.DOG_RESPAWN_DELAY,
            settings.DOG_SCORE,
        )