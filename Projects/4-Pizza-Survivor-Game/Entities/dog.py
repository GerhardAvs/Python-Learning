import pygame
import config, settings

def draw_dog(pos_x, pos_y):
        config.pantalla.blit(config.dog_img,(pos_x, pos_y))

def distance_2_delivery():
    dx = config.delivery_pos_x - config.dog_pos_x
    dy = config.delivery_pos_y - config.dog_pos_y
    
    distance = (dx**2 + dy**2)**0.5
    
    return dx, dy, distance

def moves_2_delivery(dx,dy,distance):
        if distance > 0:
                config.dog_pos_x += (dx/distance) * settings.DOG_SPEED
                config.dog_pos_y += (dy/distance) * settings.DOG_SPEED
        
    
    