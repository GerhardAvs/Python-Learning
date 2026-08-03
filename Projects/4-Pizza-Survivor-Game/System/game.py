import pygame

import config
import settings
from Entities import Cat, Dog, delivery, pizza
from System import collisions
from UI import hearts, pause_menu

dog = Dog()
cat = Cat()

class Game:
    def __init__(self):
        """constructor de la clase Game
        """
        self.playing = True
        
        config.pantalla = pygame.display.set_mode(settings.WINDOW_SIZE, pygame.FULLSCREEN)
        config.pantalla.blit(config.background, config.window_origin)
        pygame.display.set_caption("Pizza Survivor")
        pygame.display.set_icon(config.icon)

    def run(self):
        """Bucle principal del juego: maneja eventos, actualiza y dibuja.
        """
        while self.playing:
        
            self.handle_events()

            self.update()
        
            self.draw()
    
    def handle_events(self):
        """Maneja las entradas de teclado, raton para interactuar con la UI
        """
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.playing = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        config.game_paused = not config.game_paused
        
                    if not config.game_paused:
                        delivery.get_delivery_movement(event.key)
                
                if event.type == pygame.KEYUP and not config.game_paused:
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
        """Actualiza la lógica del juego: movimiento de repartidor, perro, pizzas, colisiones, etc.
        """
            #////////////////////// Si el juego está pausado, no se actualiza nada (queda "congelado") ////////////

        if not config.game_paused:
            delivery.delivery_restrictions()
            delivery.move_delivery()

            #////////////////////// Mover / respawnear al perro /////////////////////////////////////////////       
            
            pizza.move_pizzas()
            pizza.remove_offscreen_pizzas()

            #////////////////////// Detecta si alguna pizza tocó al perro (colisión por máscara) ///////////
            for enemy_instance in [dog, cat]:
                enemy_instance.update()
                collisions.resolve_pizza_enemy_collisions(enemy_instance)
                collisions.resolve_enemy_delivery_collision(enemy_instance)

    def draw(self):
        """Dibuja todos los elementos del juego en la pantalla: fondo, repartidor, perro, pizzas, corazones, menú de pausa."""
        
        #/////////////////////inicializa al repartidor, perro, pizzas, ... //////////////////////////////////
        config.pantalla.blit(config.background, config.window_origin) 
        delivery.draw_delivery(config.delivery_pos_x, config.delivery_pos_y)
        pizza.draw_pizzas()
        hearts.draw_hearts()
        for enemy_instance in [dog, cat]:
            enemy_instance.draw()

        #////////////////////// Menú de pausa (se dibuja arriba de todo) ///////////////////////////////////
        if config.game_paused:
            pause_menu.draw_pause_menu()
            
        pygame.display.update()


