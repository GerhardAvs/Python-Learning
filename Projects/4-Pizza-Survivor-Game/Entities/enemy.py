from random import choice, randint

import pygame

import config
import settings


##
# @file enemy.py
# @brief Implementa la clase base de los enemigos del juego.
#
# Este módulo define la clase Enemy, utilizada como base para
# todos los enemigos (como perros y gatos). Proporciona la
# funcionalidad común para el movimiento, dibujo, colisiones,
# reaparición y cálculo de la posición.

class Enemy:
    ##
    # @brief Clase base para los enemigos del juego.
    #
    # Cada enemigo administra su propia imagen, máscara de colisión,
    # posición, velocidad, estado de vida y tiempo de reaparición.
    # La clase está diseñada para ser heredada por tipos específicos
    # de enemigos como Dog y Cat.
    #
    # @note Cada instancia mantiene su propio estado, permitiendo
    # múltiples enemigos simultáneamente.
    def __init__(self, image_path, speed, size, respawn_delay, points):
        ##
        # @brief Inicializa un nuevo enemigo.
        #
        # @param image_path Ruta de la imagen del enemigo.
        # @param speed Velocidad de movimiento hacia el repartidor.
        # @param size Tamaño al que se escalará la imagen.
        # @param respawn_delay Tiempo de espera antes de reaparecer, en milisegundos.
        # @param points Puntaje otorgado al eliminar este enemigo.
        # @return None
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, size)
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed
        self.size = size
        self.respawn_delay = respawn_delay
        self.points = points

        self.pos_x, self.pos_y = self._spawn_outside_screen()
        self.alive = True
        self.death_time = 0

    @property
    def pos(self):
        ##
        # @brief Obtiene la posición actual del enemigo.
        #
        # @return tuple Tupla (x, y) con la posición del enemigo.
        return (self.pos_x, self.pos_y)

    ##
    # @brief Dibuja el enemigo en la pantalla.
    #
    # El enemigo solo se dibuja cuando está vivo.
    #
    # @return None
    def draw(self):
        if self.alive:
            config.pantalla.blit(self.image, (self.pos_x, self.pos_y))

    ##
    # @brief Calcula la distancia entre el enemigo y el repartidor.
    #
    # @return tuple Tupla con (dx, dy, distancia).
    def _distance_to_delivery(self):
        dx = config.delivery_pos_x - self.pos_x
        dy = config.delivery_pos_y - self.pos_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return dx, dy, distance

    ##
    # @brief Mueve el enemigo hacia el repartidor.
    #
    # El movimiento se realiza en línea recta utilizando la velocidad
    # configurada para el enemigo.
    #
    # @return None
    def _move_towards_delivery(self):
        dx, dy, distance = self._distance_to_delivery()
        if distance > 0:
            self.pos_x += (dx / distance) * self.speed
            self.pos_y += (dy / distance) * self.speed

    ##
    # @brief Elimina temporalmente al enemigo.
    #
    # Cambia el estado del enemigo a muerto e inicia el contador
    # para su futura reaparición.
    #
    # @return None
    def kill(self):
        self.alive = False
        self.death_time = pygame.time.get_ticks()

    ##
    # @brief Actualiza el estado del enemigo.
    #
    # Si el enemigo está vivo, se mueve hacia el repartidor.
    # Si está muerto y ha transcurrido el tiempo de reaparición,
    # vuelve a aparecer en un borde aleatorio de la pantalla.
    #
    # @return None
    def update(self):
        if self.alive:
            self._move_towards_delivery()
        else:
            ahora = pygame.time.get_ticks()
            if ahora - self.death_time >= self.respawn_delay:
                self.pos_x, self.pos_y = self._spawn_outside_screen()
                self.alive = True

    ##
    # @brief Genera una posición inicial fuera de la pantalla.
    #
    # Selecciona aleatoriamente uno de los cuatro bordes de la
    # ventana para que el enemigo aparezca completamente fuera
    # de la pantalla y entre caminando.
    #
    # @return tuple Tupla (x, y) con la posición inicial.
    def _spawn_outside_screen(self):
        ancho, alto = settings.WINDOW_SIZE
        borde = choice(["arriba", "abajo", "izquierda", "derecha"])

        if borde == "arriba":
            return randint(0, int(ancho - self.size[0])), -self.size[1]
        if borde == "abajo":
            return randint(0, int(ancho - self.size[0])), alto
        if borde == "izquierda":
            return -self.size[0], randint(0, int(alto - self.size[1]))
        return ancho, randint(0, int(alto - self.size[1]))