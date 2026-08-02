import pygame
import config, settings
from random import randint, choice

def draw_dog(pos_x, pos_y):
        if config.dog_alive:
                config.pantalla.blit(config.dog_img,(pos_x, pos_y))

def distance_2_delivery():
    config.dx_dog = config.delivery_pos_x - config.dog_pos_x
    config.dy_dog = config.delivery_pos_y - config.dog_pos_y
    
    config.distance_dog = (config.dx_dog**2 + config.dy_dog**2)**0.5
    
def moves_2_delivery(dx,dy,distance):
        if distance > 0:
                config.dog_pos_x += (dx/distance) * settings.DOG_SPEED
                config.dog_pos_y += (dy/distance) * settings.DOG_SPEED
        
def kill_dog():
    """Elimina al perro actual y arranca el temporizador de respawn."""
    config.dog_alive = False
    config.dog_death_time = pygame.time.get_ticks()
    
def update_dog():
    """
    Si el perro está vivo, lo mueve hacia el repartidor.
    Si está muerto, espera DOG_RESPAWN_DELAY y lo hace reaparecer
    afuera de la pantalla, en un borde random.
    """
    if config.dog_alive:
        distance_2_delivery()
        moves_2_delivery(config.dx_dog, config.dy_dog, config.distance_dog)
    else:
        ahora = pygame.time.get_ticks()
        if ahora - config.dog_death_time >= settings.DOG_RESPAWN_DELAY:
            config.dog_pos_x, config.dog_pos_y = dog_spawn_outside_screen()
            config.dog_alive = True
            
def dog_spawn_outside_screen():
    """
    Elige un punto random sobre uno de los 4 bordes de la pantalla, pero
    completamente fuera de ella (el sprite no se llega a ver), para que
    el perro "entre solo" caminando a buscar al repartidor.
    """
    ancho, alto = settings.WINDOW_SIZE
    borde = choice(["arriba", "abajo", "izquierda", "derecha"])

    if borde == "arriba":
        return randint(0, int(ancho - settings.DOG_SIZE[0])), -settings.DOG_SIZE[1]
    if borde == "abajo":
        return randint(0, int(ancho - settings.DOG_SIZE[0])), alto
    if borde == "izquierda":
        return -settings.DOG_SIZE[0], randint(0, int(alto - settings.DOG_SIZE[1]))
    return ancho, randint(0, int(alto - settings.DOG_SIZE[1]))