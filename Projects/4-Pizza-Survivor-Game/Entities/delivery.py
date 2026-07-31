import pygame
import config, settings


def draw_delivery(pos_x, pos_y):   
        """
        Initialize the delivery character on the screen at the specified position.
        
        Args:
                pos_x (int): The x-coordinate for the delivery character's position.
                pos_y (int): The y-coordinate for the delivery character's position.
        """ 
        config.pantalla.blit(config.delivery_img,(pos_x, pos_y))
        
def move_delivery():
        """
        Move the delivery character on the screen.
        
        """
        config.delivery_pos_x += config.delivery_change_pos_x
        config.delivery_pos_y += config.delivery_change_pos_y
        
def get_delivery_movement(event):
        """
        Update the delivery character's movement based on the key pressed.
        
        Args:
                event (int): The key code of the pressed key.
        """
        if event == pygame.K_a:
                config.delivery_change_pos_x = -settings.DELIVERY_SPEED
                print('izq')
        if event == pygame.K_d:
                config.delivery_change_pos_x = settings.DELIVERY_SPEED
                print('right')
        if event == pygame.K_w:
                config.delivery_change_pos_y = -settings.DELIVERY_SPEED
                print('up')
        if event == pygame.K_s:
                config.delivery_change_pos_y = settings.DELIVERY_SPEED
                print('down')
                
def reset_delivery_movement(event):
        """
        reset the delivery character's movement when the key is released.
        
        Args:
                event (int): The key code of the released key.
        """
        if event in (pygame.K_a, pygame.K_d):
                config.delivery_change_pos_x = 0
                
        if event in (pygame.K_w, pygame.K_s):
                config.delivery_change_pos_y = 0
                
def delivery_restrictions():   
        """
        Restrict the delivery character's movement within the screen boundaries.
        
        """
        if config.delivery_pos_x < 0:
                config.delivery_pos_x = 0
                
        elif config.delivery_pos_x > settings.WINDOW_SIZE[0] - settings.DELIVERY_SIZE[0]:
                config.delivery_pos_x = settings.WINDOW_SIZE[0] - settings.DELIVERY_SIZE[0]

        if config.delivery_pos_y < 0:
                config.delivery_pos_y = 0

        elif config.delivery_pos_y > settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1]:
                config.delivery_pos_y = settings.WINDOW_SIZE[1] - settings.DELIVERY_SIZE[1]