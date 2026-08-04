import pygame

import config
import settings
from Entities.enemy import Enemy

##
# @file cat.py
# @brief Define la clase Cat.
#
# Este módulo implementa la clase Cat, que representa un enemigo
# de tipo gato. Hereda el comportamiento general de la clase Enemy
# y únicamente establece sus atributos específicos.

class Cat(Enemy):
    ##
    # @brief Crea una nueva instancia de un gato.
    #
    # Inicializa el enemigo con la configuración específica para los
    # gatos, incluyendo su sprite, velocidad, tamaño, tiempo de
    # reaparición y puntaje otorgado al ser eliminado.
    #
    # @return None
    def __init__(self):
        super().__init__(
            config.cat_path,
            settings.CAT_SPEED,
            settings.CAT_SIZE,
            settings.CAT_RESPAWN_DELAY,
            settings.CAT_SCORE,
        )