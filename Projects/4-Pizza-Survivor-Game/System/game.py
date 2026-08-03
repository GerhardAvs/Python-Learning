import pygame

import config
from Entities import delivery,dog, pizza
from UI import hearts, pause_menu
from System import collisions

class Game():
    def __init__(self):
        self.playing = True
 
    def running(self):
        while self.playing:
        
            self.handle_events()

            self.update()
        
            self.draw()
    
    def handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.playing = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        config.game_paused = not config.game_paused
                    if event.key == pygame.K_e:
                        ... #Despliega menu de poderes (no implementado)
        
                    if not config.game_paused:
                        delivery.get_delivery_movement(event.key)
                
                if event.type == pygame.KEYUP:
                    if not config.game_paused:
                        delivery.reset_delivery_movement(event.key)
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if config.game_paused:
                        if event.button == 1: #Clic izquierdo del mouse
                            accion = pause_menu.handle_menu_click(event.pos)
                            if accion == "reanudar":
                                config.game_paused = False
                            elif accion == "salir":
                                self.playing = False
                            elif accion == "traje":
                                ... #Cambiar de traje (no implementado)
                    else:
                        if event.button == 1: #Clic izquierdo del mouse
                            pizza.launch_pizza(event.pos)
                        elif event.button == 2: #Clic derecho del mouse
                            ... #Despliega algun poder especial del repartidor que se encuentre en el suelo (no implementado)
        
    def update(self):
            #////////////////////// Si el juego está pausado, no se actualiza nada (queda "congelado") ////////////
        if not config.game_paused:
            #////////////////////// Mueve y restringe al repartidor //////////////////////////////////////////       
            delivery.delivery_restrictions()
            delivery.move_delivery()
            
            #////////////////////// Mover / respawnear al perro /////////////////////////////////////////////       
            dog.update_dog()
            
            #////////////////////// Mover pizzas y limpiar las que salieron de pantalla /////////////////////
            pizza.move_pizzas()
            pizza.remove_offscreen_pizzas()

            #////////////////////// Detecta si alguna pizza tocó al perro (colisión por máscara) ///////////
            collisions.resolve_pizza_dog_collisions()

            #////////////////////// Detecta si el perro tocó al repartidor (resta una vida) /////////////////
            collisions.resolve_dog_delivery_collision()
                        
    def draw(self):
        #/////////////////////inicializa al repartidor, perro, pizzas, ... //////////////////////////////////
        config.pantalla.blit(config.background, config.window_origin) 
        delivery.draw_delivery(config.delivery_pos_x, config.delivery_pos_y)
        dog.draw_dog(config.dog_pos_x, config.dog_pos_y)
        pizza.draw_pizzas()
        hearts.draw_hearts()

        #////////////////////// Menú de pausa (se dibuja arriba de todo) ///////////////////////////////////
        if config.game_paused:
            pause_menu.draw_pause_menu()
        pygame.display.update()


