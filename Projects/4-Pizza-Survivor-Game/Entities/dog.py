import pygame
import config, settings

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
            config.dog_pos_x, config.dog_pos_y = config.dog_spawn_outside_screen()
            config.dog_alive = True