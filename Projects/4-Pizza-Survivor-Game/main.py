import pygame

#initializa pygame
pygame.init()

import config, settings
from Entities import delivery,dog
from UI import button_salir


#Loop del juego 
still_playing = True
config.pantalla = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.FULLSCREEN)


config.pantalla.blit(config.background, config.window_origin)

pygame.display.set_caption("Pizza Survivor")
pygame.display.set_icon(config.icon)

while still_playing:
    #////////////////////// Obtiene eventos del juego //////////////////////////////////////////////       
    for event in pygame.event.get():
        #Detecta si se cierra la ventana
        if event.type == pygame.QUIT: 
            still_playing = False
            
        #Detecta si se presiono una tecla
        if event.type == pygame.KEYDOWN:
            print(event.key)
            delivery.get_delivery_movement(event.key)
        
        if event.type == pygame.KEYUP:
            delivery.reset_delivery_movement(event.key)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            still_playing = button_salir.exit_button(event.pos)
            
            
    #////////////////////// ponemos el fondo en la pantalla //////////////////////////////////////////////       
    config.pantalla.blit(config.background, config.window_origin)     
    
    #////////////////////// Mueve y restringe al repartidor //////////////////////////////////////////////       
    delivery.delivery_restrictions()
    delivery.move_delivery()
    
    #////////////////////// Mover al perro //////////////////////////////////////////////////////////////       
    dx,dy,distance = dog.distance_2_delivery()
    dog.moves_2_delivery(dx,dy,distance)
    

    #/////////////////////inicializa al repartidor, perro, gato, ... //////////////////////////////////////
    delivery.draw_delivery(config.delivery_pos_x, config.delivery_pos_y)
    dog.draw_dog(config.dog_pos_x, config.dog_pos_y)
    button_salir.draw_exit_button(config.btnSalir_pos_x, config.btnSalir_pos_y)
    pygame.display.update()

pygame.quit()