import pygame

import settings
import utilities

class BaseEnemy(pygame.sprite.Sprite):
    """
    Base enemy class.
    """
    def __init__(self, game_board):
        pygame.sprite.Sprite.__init__(self)
        
        self.game_board = game_board
        
        image_file_path = settings.BASE_ENEMY_IMAGE_PATH
        self.image , self.rect = utilities.load_image(image_file_path)
        
        self.rect.center = self.game_board.get_enemy_spawn()
        
        #Declare some variables:
        self.movement_per_press = settings.PLAYER_MOVE_SPEED
        self.current_direction = settings.D_UP
    
    