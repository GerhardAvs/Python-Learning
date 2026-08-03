from random import choice, randint

import pygame

import config
import settings


class Enemy:
    """
    Clase base para un enemigo que persigue al repartidor.

    Es autocontenida: carga su propia imagen, escala y máscara de
    colisión, y guarda su propio estado (posición, vivo/muerto, tiempo
    de muerte). No depende de variables globales tipo config.dog_*,
    por lo que puede instanciarse varias veces (perro, gato, etc.)
    sin que una instancia pise el estado de otra.
    """

    def __init__(self, image_path, speed, size, respawn_delay):
        """
        Args:
            image_path (str): ruta de la imagen del enemigo.
            speed (int|float): velocidad de movimiento hacia el repartidor.
            size (tuple[int, int]): tamaño (ancho, alto) al que se escala la imagen.
            respawn_delay (int): milisegundos que tarda en reaparecer tras morir.
        """
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.smoothscale(self.image, size)
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = speed
        self.size = size
        self.respawn_delay = respawn_delay

        self.pos_x, self.pos_y = self._spawn_outside_screen()
        self.alive = True
        self.death_time = 0

    @property
    def pos(self):
        """Posición actual como tupla (x, y), útil para colisiones."""
        return (self.pos_x, self.pos_y)

    def draw(self):
        """Dibuja al enemigo en pantalla si está vivo."""
        if self.alive:
            config.pantalla.blit(self.image, (self.pos_x, self.pos_y))

    def _distance_to_delivery(self):
        """Calcula (dx, dy, distancia) desde el enemigo hasta el repartidor."""
        dx = config.delivery_pos_x - self.pos_x
        dy = config.delivery_pos_y - self.pos_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        return dx, dy, distance

    def _move_towards_delivery(self):
        """Mueve al enemigo un paso (según su velocidad) hacia el repartidor."""
        dx, dy, distance = self._distance_to_delivery()
        if distance > 0:
            self.pos_x += (dx / distance) * self.speed
            self.pos_y += (dy / distance) * self.speed

    def kill(self):
        """Mata al enemigo y arranca el temporizador de respawn."""
        self.alive = False
        self.death_time = pygame.time.get_ticks()

    def update(self):
        """
        Si el enemigo está vivo, lo mueve hacia el repartidor.
        Si está muerto, espera respawn_delay y lo hace reaparecer
        afuera de la pantalla, en un borde random.
        """
        if self.alive:
            self._move_towards_delivery()
        else:
            ahora = pygame.time.get_ticks()
            if ahora - self.death_time >= self.respawn_delay:
                self.pos_x, self.pos_y = self._spawn_outside_screen()
                self.alive = True

    def _spawn_outside_screen(self):
        """
        Elige un punto random sobre uno de los 4 bordes de la pantalla, pero
        completamente fuera de ella (el sprite no se llega a ver), para que
        el enemigo "entre solo" caminando a buscar al repartidor.
        """
        ancho, alto = settings.WINDOW_SIZE
        borde = choice(["arriba", "abajo", "izquierda", "derecha"])

        if borde == "arriba":
            return randint(0, int(ancho - self.size[0])), -self.size[1]
        if borde == "abajo":
            return randint(0, int(ancho - self.size[0])), alto
        if borde == "izquierda":
            return -self.size[0], randint(0, int(alto - self.size[1]))
        return ancho, randint(0, int(alto - self.size[1]))